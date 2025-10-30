import requests


def emotion_detector(text_to_analyze):
    """Detect emotion from the input text using the Emotion Predict
    function of the Watson NLP Library.
    """
    # URL endpoint for accessing the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Request headers required by the Emotion Predict function
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    
    # Input data sent to the Emotion Predict function
    input_data = {'raw_document': {'text': text_to_analyze}}

    # Send POST request to the Emotion Predict function and receive response
    response = requests.post(url, json=input_data, headers=headers)

    # Return text value from the received response
    return response.text

