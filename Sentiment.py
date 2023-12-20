
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def Get_Senti(text: str) -> str:
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)

    if sentiment["compound"] >= 0.1:
        return "Positive"

    elif sentiment["compound"] <= -0.1:
        return "Negative"

    else:
        return "Neutral"
    


# print(Get_Senti("Government has taken various policy decisions and initiatives to increase the share of indian seafarers at global level: shri mansukh mandaviya."))
