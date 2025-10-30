import json
import requests


def emotion_detector(text_to_analyze):
    """Detect emotion from the input text using the Emotion Predict
    function of the Watson NLP Library."""

    # URL endpoint for accessing the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Request headers required by the Emotion Predict function
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}

    # Request data sent to the Emotion Predict function
    request_data = {'raw_document': {'text': text_to_analyze}}

    # Send POST request to the Emotion Predict function and receive response
    response = requests.post(url, json=request_data, headers=headers)

    # Handle failed response with status code 400
    if response.status_code == 400:
        # Return data struct with `None` values
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    # Convert the response text into a dictionary
    data = json.loads(response.text)

    # Extract emotions from the response data and store as output data
    output_data = data['emotionPredictions'][0]['emotion']

    # Sort emotions in reversed order using score as the sorting key.
    sorted_data = sorted(output_data.items(), key=lambda i: i[1], reverse=True)

    # Store the dominant emotion's name to the output data, which is the first
    # item found in the sorted list of emotions.
    output_data['dominant_emotion'] = sorted_data[0][0]

    # Return the output data
    return output_data
