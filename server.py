'''to define emotions'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''to send get emotion detector request'''
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return "describes "+dominant_emotion

@app.route("/")
def render_index_page():
    '''to render index.html'''
    return render_template('index.html')

app.run(host="0.0.0.0", port=5000)
