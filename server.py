"""
This module contains the Flask web server for the Emotion Analyzer application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the provided text for emotion and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.pop('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    formatted_data = ", ".join(
        f"'{key}': {value}" for key, value in response.items()
    )
    return (
        f"For the given statement, the system response is {{{formatted_data}}}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
