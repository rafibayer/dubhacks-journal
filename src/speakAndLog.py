from textRecorder import TextRecorder
from speechToText import STT

class SpeakAndLog():


    # creates a new SpeakAndLog object
    # contains a TextRecorder and a Speach to Text (STT)
    def __init__(self):
        self.tr = TextRecorder()
        self.stt = STT()
        self.tr.serialize_data(self.tr.filepath)

    # record and log a new entry
    def new_stt_entry(self):
        entry = self.stt.speech_to_text() # get list of phrases
        result = " ".join(entry) # join into one string
        self.tr.add_entry(result) # log in TextRecorder
        self.tr.serialize_data(self.tr.filepath) # save TextRecorder
        


