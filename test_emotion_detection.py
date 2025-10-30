import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case 1: statement with joy emotion
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

        # Test case 2: statement with anger emotion
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

        # Test case 3: statement with disgust emotion
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

        # Test case 4: statement with sadness emotion
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

        # Test case 5: statement with fear emotion
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    # Run unittest when executed directly
    unittest.main()
