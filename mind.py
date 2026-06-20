import json
import glob
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


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
            continue  # opinionsが空なら除外
        
        last_polarity = opinions[-1]["polarity"]  # 最後の意見の極性
        
        if last_polarity == "positive":
            texts.append(s["sentence"])
            labels.append(1)
        elif last_polarity == "negative":
            texts.append(s["sentence"])
            labels.append(0)
        # neutralの場合は何もしない(除外)

vectorizer = CountVectorizer(tokenizer=tokenize)
X = vectorizer.fit_transform(texts)
y = labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y)

model = MultinomialNB()
model.fit(X_train, y_train)

print("精度:", model.score(X_test, y_test))
print("件数:", len(texts))
print("ポジティブ件数:", labels.count(1))
print("ネガティブ件数:", labels.count(0))