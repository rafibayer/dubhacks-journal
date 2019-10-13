from flask import Flask, request
from speechToText import STT
from camera import Camera
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







if __name__ == "__main__":
    app.run()