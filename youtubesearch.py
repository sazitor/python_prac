import os
import re
import json
import glob
from html import unescape
from dotenv import load_dotenv
from googleapiclient.discovery import build
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from langdetect import detect, LangDetectException
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Meiryo'

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

if api_key is None:
    print("エラー: APIキーが見つかりません。.envファイルを確認してください。")
    exit()

youtube = build("youtube", "v3", developerKey=api_key)

def clean_comment(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    text = re.sub(r'https?://\S+', '', text)
    text = text.strip()
    return text

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
    model = MultinomialNB()
    model.fit(X, labels)
    print("モデル学習完了")
    return model, vectorizer

def search_videos(keyword):
    search_request = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=5
    )
    search_response = search_request.execute()
    video_ids = []
    for item in search_response["items"]:
        video_ids.append(item["id"]["videoId"])
    return video_ids


def get_comments(video_ids):
    all_comments = []
    for video_id in video_ids:
        try:
            comment_request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=20
            )
            comment_response = comment_request.execute()
            for item in comment_response["items"]:
                comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                try:
                    if detect(comment) == "ja":
                        all_comments.append(comment)
                except LangDetectException:
                    continue
        except Exception as e:
            print(f"動画ID {video_id} のコメント取得に失敗: {e}")
            continue
    return all_comments

def analyze_comments(comments, model, vectorizer):
    print("\n--- 感情分析結果 ---")
    positive_count = 0
    negative_count = 0
    for comment in comments:
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

def show_graph(positive_count, negative_count, keyword):
    labels = ["ポジティブ", "ネガティブ"]
    counts = [positive_count, negative_count]
    colors = ["#4CAF50", "#F44336"]
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title(f"「{keyword}」のYouTubeコメント感情分析結果")
    plt.show()

# メイン処理
keyword = input("検索キーワードを入力してください: ")
model, vectorizer = load_model()
video_ids = search_videos(keyword)
print(f"取得した動画ID: {video_ids}")
comments = get_comments(video_ids)
print(f"取得したコメント数: {len(comments)}")

if len(comments) == 0:
    print("コメントが取得できませんでした。")
    exit()

positive_count, negative_count = analyze_comments(comments, model, vectorizer)
show_graph(positive_count, negative_count, keyword)