from flask import Flask, request, jsonify, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly
import plotly.graph_objects as go
import plotly.utils
import json

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')

    # Perform sentiment analysis
    scores = analyze_sentiment(text)

    # Generate Plotly graph dynamically
    fig = go.Figure([go.Bar(
        x=['Negative', 'Neutral', 'Positive'],
        y=[scores['neg'], scores['neu'], scores['pos']],
        marker_color=['red', 'gray', 'green']
    )])
    fig.update_layout(title="Sentiment Distribution", xaxis_title="Sentiment", yaxis_title="Score")

    # Convert Plotly figure to JSON format (NOT raw HTML)
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return jsonify({'scores': scores, 'graph_json': graph_json})

if __name__ == '__main__':
    app.run(debug=True)