# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-python-text-to-speech

import os
import requests
import time
from xml.etree import ElementTree

class TextToSpeech(object):

    # string subsription_key: api key for azure tts
    # string text: text to be converted to speech
    # saves an audio file containing speech of the passed text
    def __init__(self, subscription_key, text):
        self.subscription_key = subscription_key
        self.tts = text
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None

    def get_token(self):
        fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio(self):
        base_url = 'https://westus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'EmotionSpeech'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
        voice.set(
            'name', 'Microsoft Server Speech Text to Speech Voice (en-US, en-US-JessaRUS)') # TODO: pick voice 
        voice.text = self.tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)
        if response.status_code == 200:
            with open('sample-' + self.timestr + '.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) +
                    "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) +
                "\nSomething went wrong. Check your subscription key and headers.\n")

if __name__ == "__main__":
    subscription_key = ""
    with open("src/keys/tts_key.txt", 'r') as key_file:
        subscription_key = key_file.read()

    app = TextToSpeech(subscription_key, "test text")
    app.get_token()
    app.save_audio()