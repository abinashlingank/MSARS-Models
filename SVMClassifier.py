import openai
from Constants import Pattern
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib  


df = pd.read_csv("Data/data-1.csv")

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['department'], test_size=0.2, random_state=42)

tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

svm_classifier = SVC(kernel='linear', C=1)
svm_classifier.fit(X_train_tfidf, y_train)

def depclass(sentence):
    pattern = Pattern+ f"{sentence}"
    openai.api_key="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"
    stream=openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"assistant","content":pattern}],
        max_tokens=50,
        stream=True
    )
    xr=""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            xr+=chunk.choices[0].delta.content
    # print(xr)
    reply = xr.split('\n')
    return reply[0].split(':')[1].strip(), reply[1].split(':')[1].strip(), reply[2].split(':')[1].strip()
# print(depclass("Education policy of india is very bad"))