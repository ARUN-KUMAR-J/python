from textblob import TextBlob
text="good short"
analyse=TextBlob(text)
sentiment=analyse.sentiment.polarity
if sentiment>0:
    print("Positive Statement")
    print(sentiment)
elif sentiment<0:
    print("Negative Statement")
    print(sentiment)
else:
    print("Neutral Statement")