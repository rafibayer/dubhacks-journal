'''
https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-python

USAGE:
Create new STT instance: stt = STT()

start recording and return list of phrases once speech stops

results = stt.speech_to_text()
'''

import azure.cognitiveservices.speech as speechsdk

class STT():

    # initialize the speech to text sdk
    def __init__(self):
        # Creates an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").
        my_key = "2506a837cb0945bf9ad6c315b683291b"
        speech_key, service_region = my_key, "westus"
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

        # Creates a recognizer with the given settings
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

    # records phrases until you stop talking
    # returns a list of phrases
    def speech_to_text(self):

        print("Say something...")


        # Starts speech recognition, and returns after a single utterance is recognized. The end of a
        # single utterance is determined by listening for silence at the end or until a maximum of 15
        # seconds of audio is processed.  The task returns the recognition text as result. 
        # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
        # shot recognition like command or query. 
        # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
        result = []
        nextText = "START"
        while nextText.strip() != "":
            nextResult = self.speech_recognizer.recognize_once()
            nextText = nextResult.text
            print(nextText)
            result.append(nextText)

        return result

        # can be used for validation, from original code sample
        # # Checks result.
        # if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        #     print("returning recognized speech...")
        #     return result.text
        # elif result.reason == speechsdk.ResultReason.NoMatch:
        #     print("No speech could be recognized: {}".format(result.no_match_details))
        # elif result.reason == speechsdk.ResultReason.Canceled:
        #     cancellation_details = result.cancellation_details
        #     print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        #     if cancellation_details.reason == speechsdk.CancellationReason.Error:
        #         print("Error details: {}".format(cancellation_details.error_details))


stt = STT()
stt.speech_to_text()