'''
USAGE:
GET/SET word: get and set the net sentiment for passed word
    Used for Sina's text analysis

GET/SET day_emotion: get and set the emotion for a day
    Used for Dana's face emotion recognizer

GET/SET day_text: get and set for text journal entry for a day
    Used for Rafi's speech to text


THINGS YOU NEED:
A file called data.txt in src/data/

    if you want to use a different file, create it and filepath it into
    constructor filepath parameter
'''

import json
import sys
import os


class Storage:

    # create instance of storage
    # optionally pass a filepath, otherwise it uses the default
    def __init__(self, filepath="src/data/data.txt"):
        self.filepath = filepath


        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Create a storage file, default path: {self.filepath}")

        with open(self.filepath, "r") as json_file:
            self.data = json.loads(json_file.read())

    # used internally to write to file after operations
    def serialize(self):
        with open(self.filepath, 'w+') as json_file:
            json.dump(self.data, json_file)

    # string word: word to get the value of
    # return int: net sentiment value for the passed word
    # if word is not found, create it with a value of 0 and return 0
    def get_word(self, word):
        if word in self.data["wordSentiments"].keys():
            return int(self.data["wordSentiments"][word])

        else:
            self.data["wordSentiments"][word] = '0'
            self.serialize()
            return 0

    # string word: word to update the value of
    # int val: new value for the word
    def set_word(self, word, val):
        self.data["wordSentiments"][word] = str(val)
        self.serialize()

    def get_day_emotion(self, day):
        day = str(day)
        if day in self.data["dayEmotions"].keys():
            return self.data["dayEmotions"][day]

        else:
            self.data["dayEmotions"][day] = "None"
            self.serialize()
            return "None"


    def set_day_emotion(self, day, emotion):
        day = str(day)
        emotion = str(emotion)
        self.data["dayEmotions"][day] = emotion
        self.serialize()


    def get_day_text(self, day):
        day = str(day)
        if day in self.data["dayText"].keys():
            return self.data["dayText"][day]

        else:
            self.data["dayText"][day] = "None"
            self.serialize()
            return "None"

    def set_day_text(self, day, text):
        day = str(day)
        text = str(text)
        self.data["dayText"][day] = text
        self.serialize()

S = Storage()
S.set_day_text(31, "Happy Halloween")



