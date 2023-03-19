from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = analyze_sentiment(text)
    return {"sentiment": sentiment}


def analyze_sentiment(text):
    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment


if __name__ == '__main__':
    app.run(debug=True)

