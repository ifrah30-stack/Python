from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pandas as pd

df = pd.read_csv("news.csv")  # columns: text, label
tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(df["text"])
y = df["label"]
model = PassiveAggressiveClassifier().fit(X, y)
print("Model trained!")
