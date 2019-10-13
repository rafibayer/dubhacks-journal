from flask import Flask, request, jsonify
from speechToText import STT
from camera import Camera
from analysisPipeline import AnalysisPipeline
from visualize import Viz
import os



app = Flask(__name__)


@app.route("/get_stt/", methods=['GET'])
def call_stt():
    my_stt = STT()
    result = my_stt.speech_to_text()

    print(' '.join(result))
    return ' '.join(result)


@app.route("/take_picture/", methods=['GET'])
def call_camera():
    my_cam = Camera()
    result = my_cam.getEmotion()

    print(result)
    return result

@app.route("/run_text_analysis/", methods=['GET'])
def call_ap():
    my_ap = AnalysisPipeline()

    result = my_ap.getAndAnalyzeSpeech()

    print(result)
    return result


@app.route("/get_happy_sad/", methods=['GET'])
def call_happy_sad():
    my_vis = Viz()
    result = my_vis.happy_or_sad()
    print(result)
    return result

@app.route("/get_word_assoc/", methods=['GET'])
def call_word_assoc():
    my_vis = Viz()
    result = my_vis.wordAssociation()
    print(result)
    return jsonify(result)


if __name__ == "__main__":
    app.run()