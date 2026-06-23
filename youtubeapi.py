import os
import re
import json
import glob
from html import unescape
from dotenv import load_dotenv
from googleapiclient.discovery import build
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォント設定(Windows)
plt.rcParams['font.family'] = 'Meiryo'
# YouTube API設定
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

if api_key is None:
    print("エラー: APIキーが見つかりません。.envファイルを確認してください。")
    exit()

youtube = build("youtube", "v3", developerKey=api_key)

# コメント前処理
def clean_comment(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    text = re.sub(r'https?://\S+', '', text)
    text = text.strip()
    return text

# 感情分析モデルの学習
def load_model():
    t = Tokenizer()
    
    def tokenize(text):
        return [token.surface for token in t.tokenize(text)]
    
    texts = []
    labels = []
    
    files = glob.glob("chabsa-dataset/chABSA-dataset/*.json")
    
    for file in files:
        with open(file, encoding="utf-8") as f:
            data = json.load(f)
        for s in data["sentences"]:
            opinions = s["opinions"]
            if len(opinions) == 0:
                continue
            last_polarity = opinions[-1]["polarity"]
            if last_polarity == "positive":
                texts.append(s["sentence"])
                labels.append(1)
            elif last_polarity == "negative":
                texts.append(s["sentence"])
                labels.append(0)
    
    vectorizer = CountVectorizer(tokenizer=tokenize)
    X = vectorizer.fit_transform(texts)
    y = labels
    
    model = MultinomialNB()
    model.fit(X, y)
    
    print("モデル学習完了")
    return model, vectorizer


def get_comments(video_id):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=10
    )
    try:
        response = request.execute()
        return response["items"]
    except Exception as e:
        print(f"エラー: YouTubeAPIのリクエストに失敗しました。{e}")
        return None


def analyze_comments(comments):
    print("\n--- 感情分析結果 ---")
    positive_count = 0
    negative_count = 0

    for item in comments:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        clean = clean_comment(comment)
        if len(clean) == 0:
            continue
        X_comment = vectorizer.transform([clean])
        prediction = model.predict(X_comment)[0]
        label = "ポジティブ" if prediction == 1 else "ネガティブ"
        if prediction == 1:
            positive_count += 1
        else:
            negative_count += 1
        print(f"[{label}] {clean[:30]}...")

    print("\n--- 集計結果 ---")
    total = positive_count + negative_count

    if total == 0:
        print("分析できるコメントがありませんでした。")
    else:
        print(f"ポジティブ: {positive_count}件 ({positive_count/total*100:.1f}%)")
        print(f"ネガティブ: {negative_count}件 ({negative_count/total*100:.1f}%)")

    return positive_count, negative_count
        # 集計結果をグラフ化

def show_graph(positive_count, negative_count):

    labels = ["ポジティブ", "ネガティブ"]
    counts = [positive_count, negative_count]
    colors = ["#4CAF50", "#F44336"]

    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title("YouTubeコメント感情分析結果")    
    plt.show()  

model, vectorizer = load_model()
comment = get_comments("tCMl1AWfhQQ")  # 動画IDを指定

if comment is None:
    exit()

positive_count, negative_count = analyze_comments(comment)
show_graph(positive_count, negative_count)

