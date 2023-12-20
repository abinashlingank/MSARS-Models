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

joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')
joblib.dump(svm_classifier, 'svm_classifier.pkl')