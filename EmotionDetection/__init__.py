import json
import requests


def emotion_detector(text_to_analyze):
    """Detect emotion from the input text using the Emotion Predict
    function of the Watson NLP Library."""

    # URL endpoint for accessing the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Request headers required by the Emotion Predict function
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    
    # Input data sent to the Emotion Predict function
    input_data = {'raw_document': {'text': text_to_analyze}}

    # Send POST request to the Emotion Predict function and receive response
    response = requests.post(url, json=input_data, headers=headers)

    # Convert the response text into a dictionary
    data = json.loads(response.text)

    # Extract the set of emotions from the dictionary data
    emotion_data = data['emotionPredictions'][0]['emotion']

    # Loop through each item in the emotion data and find one whose score is dominant
    dominant_name, dominant_score = '', 0
    for name, score in emotion_data.items():
        if score > dominant_score:
            dominant_score = score
            dominant_name = name

    # Write the dominant emotion's name having found to the emotion data
    emotion_data['dominant_emotion'] = dominant_name

    # Return emotion data
    return emotion_data
    