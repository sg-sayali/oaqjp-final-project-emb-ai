"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import Mock, patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def check_emotion(self, dominant):
        emotions = {
            "anger": 0.05,
            "disgust": 0.05,
            "fear": 0.05,
            "joy": 0.05,
            "sadness": 0.05,
        }
        emotions[dominant] = 0.80

        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{"emotion": emotions}]
        }

        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=response,
        ):
            result = emotion_detector("Test emotion")

        self.assertEqual(result["dominant_emotion"], dominant)

    def test_anger(self):
        self.check_emotion("anger")

    def test_disgust(self):
        self.check_emotion("disgust")

    def test_fear(self):
        self.check_emotion("fear")

    def test_joy(self):
        self.check_emotion("joy")

    def test_sadness(self):
        self.check_emotion("sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        response = Mock()
        response.status_code = 400
        mock_post.return_value = response
        result = emotion_detector("Invalid input")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
