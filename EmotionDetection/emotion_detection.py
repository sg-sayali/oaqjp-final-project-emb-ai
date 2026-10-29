"""Detect emotions using the Watson Emotion Detection API."""

import requests


def emotion_detector(text_to_analyse):
    """Return emotion scores and the dominant emotion."""
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return empty_result

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(
            url, json=payload, headers=headers, timeout=30
        )
    except requests.RequestException:
        return empty_result

    if response.status_code == 400:
        return empty_result

    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]

    result = {
        key: emotions[key]
        for key in ("anger", "disgust", "fear", "joy", "sadness")
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result
