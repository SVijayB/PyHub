from textblob import TextBlob

text = "I love using TextBlob."
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment > 0:
    print("Positive")
elif sentiment == 0:
    print("Neutral")
else:
    print("Negative")

text = "I hate Mondays."
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment > 0:
    print("Positive")
elif sentiment == 0:
    print("Neutral")
else:
    print("Negative")

with open("example.txt", "r") as f:
    text = f.read()
blob = TextBlob(text)
polarity = blob.sentiment.polarity
print(polarity)
