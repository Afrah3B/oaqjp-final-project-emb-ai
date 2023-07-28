import unittest 
from emotion_detection import emotion_detector

class tests(unittest.TestCase):
    def test1(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result, 'joy')
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result, 'anger') 
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result, 'disgust')
        result = emotion_detector("I am so sad about this") 
        self.assertEqual(result, 'sadness') 
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result, 'fear')
          
unittest.main()
