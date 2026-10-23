# in git hub u-untracked
#uam 
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

text = input("Enter a sentence: ")

score = sia.polarity_scores(text)

if score["compound"] >= 0.05:
    print("Positive Sentiment 😊")
elif score["compound"] <= -0.05:
    print("Negative Sentiment 😞")
else:
    print("Neutral Sentiment 😐")

print("Sentiment Scores:", score)
