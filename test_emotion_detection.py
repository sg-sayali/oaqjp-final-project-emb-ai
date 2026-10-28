import unittest
from unittest.mock import patch, Mock
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"emotionPredictions": [{"emotion": {
            "anger": 0.01, "disgust": 0.01, "fear": 0.01,
            "joy": 0.95, "sadness": 0.02}}]}
        mock_post.return_value = response
        self.assertEqual(emotion_detector("I am happy")["dominant_emotion"], "joy")

if __name__ == "__main__":
    unittest.main()
