import requests

def emotion_detector(text):
    if not isinstance(text, str) or not text.strip():
        return {"anger": None, "disgust": None, "fear": None,
                "joy": None, "sadness": None, "dominant_emotion": None}

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json={"raw_document": {"text": text}},
                             headers=headers, timeout=30)

    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None,
                "joy": None, "sadness": None, "dominant_emotion": None}

    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    result = {key: emotions[key] for key in
              ["anger", "disgust", "fear", "joy", "sadness"]}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
