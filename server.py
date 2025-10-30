from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Instantiate Flask app
app = Flask('Emotion Detection')


@app.route('/emotionDetector')
def run_emotion_detector():
    """Reads text from URL query string and passes the text to the emotion_detector
    for analyzing. Prepares and returns analysis result when done."""

    # Read input text from URL query string
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to emotion_detector for analyzing
    emotion_data = emotion_detector(text_to_analyze)

    # Read domimant emotion and remove it from the dictionary data
    dominant_emotion = emotion_data.pop('dominant_emotion')

    # Handle invalid text inputted
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'

    # Read emotion values from data and present them under a string of emotion pairs.
    emotion_pairs = [f'{name!r}: {score}' for name, score in emotion_data.items()]
    emotion_str = ', '.join(emotion_pairs[:-1]) + ' and ' + emotion_pairs[-1]

    # Return the resulted analysis text
    return (
        f'For the givent statement, the system response is {emotion_str}. '
        f'The dominant emotion is {dominant_emotion}.'
    )


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    # Run the app
    app.run(host='0.0.0.0', port=5000)
