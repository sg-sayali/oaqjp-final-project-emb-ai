"""Flask web server for the Emotion Detector."""

import requests
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Analyze submitted text and return emotion results."""
    text = request.values.get("textToAnalyze", "").strip()

    if not text:
        return "Invalid input! Try again.", 400

    try:
        result = emotion_detector(text)
    except (
        requests.RequestException,
        KeyError,
        IndexError,
        ValueError,
        TypeError,
    ):
        return "Unable to analyze text. Please try again.", 500

    if result["dominant_emotion"] is None:
        return "Invalid input! Try again.", 400

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
