import requests
import json

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Analyze the emotion of the input text using an external service.
    
    Args:
        text_to_analyze (str): The text to analyze for emotion.

    Returns:
        dict: A dictionary containing emotion predictions.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]

    return {
        'anger': emotion_predictions['anger'],
        'disgust': emotion_predictions['disgust'],
        'fear': emotion_predictions['fear'],
        'joy': emotion_predictions['joy'],
        'sadness': emotion_predictions['sadness'],
        'dominant_emotion': dominant_emotion
    }