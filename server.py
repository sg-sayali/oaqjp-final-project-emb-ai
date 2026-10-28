from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    text = request.values.get("textToAnalyze", "").strip()

    if not text:
        return "Invalid text! Please try again!", 400

    try:
        result = emotion_detector(text)

        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again!", 400

        return (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    except Exception:
        return "Unable to analyze the text. Please try again.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
