"""Flask web server for the Emotion Detector."""
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
        return "Invalid text! Please try again!", 400
    try:
        result = emotion_detector(text)
        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again!", 400
        return str(result)
    except Exception:
        return "Unable to analyze text. Please try again.", 500

if __name__ == "__main__":
    app.run(debug=False, port=5000)
