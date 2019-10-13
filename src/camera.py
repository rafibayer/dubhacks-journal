import cv2
import requests
import base64
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from storage import Storage
import io

# Camera class that takes a photo and returns an emotion analyzed with
# Azure emotion detection.
class Camera():
    def getEmotion(self):
        db = Storage()

        cam = cv2.VideoCapture(0)
        cv2.namedWindow('Press space to take a photo')

        while True:
            ret, frame = cam.read()
            cv2.imshow('Press space to take a photo', frame)
                
            key = cv2.waitKey(1)

            # If the spacebar is pressed...
            if key % 256 == 32:
                emotion = self.analyze(frame)
                break

        # Free resources
        cam.release()
        cv2.destroyAllWindows()
        dayNum = db.get_next_day()
        db.set_day_emotion(dayNum, emotion)
        return emotion

    # Takes emotion values from face detection.
    # Finds and returns the emotion with highest likelihood.
    def best_emotion(self, emotion):
        emotions = {}
        emotions['anger'] = emotion.anger
        emotions['contempt'] = emotion.contempt
        emotions['disgust'] = emotion.disgust
        emotions['fear'] = emotion.fear
        emotions['happiness'] = emotion.happiness
        emotions['neutral'] = emotion.neutral
        emotions['sadness'] = emotion.sadness
        emotions['surprise'] = emotion.surprise
        return max(zip(emotions.values(), emotions.keys()))[1]

    # Takes an image and does emotion analysis with Azure.
    def analyze(self, frame):
        face_api_endpoint = 'https://dubhacks2019.cognitiveservices.azure.com'
        face_api_key = 'bb48e70d73854c64ae9a1bc1ddc96794'

        # Prove that we are authorized to use this service account
        credentials = CognitiveServicesCredentials(face_api_key)

        # Create a FaceClient
        face_client = FaceClient(face_api_endpoint, credentials=credentials)

        img = cv2.imencode('.jpg', frame)[1]

        # 'image' contains the image as base64 encoded text. 
        # this code converts the value back into binary data.
        base64_image = base64.b64decode(base64.b64encode(img).decode())

        # Face Client can't process raw binary data directly, so we convert it to a stream.
        image = io.BytesIO(base64_image)

        # The Face Client detects faces and returns them, as well as emotion for the faces.
        faces = face_client.face.detect_with_stream(image, return_face_attributes=['emotion'])
        
        return self.best_emotion(faces[0].face_attributes.emotion)



# c = Camera()
# print(c.getEmotion())