from speechToText import STT
from textAnalysis import TextAnalysis

class AnalysisPipeline:
    def __init__(self):
        self.stt = STT()
        self.sadThreshold = 0.33
        self.happyThreshold = 0.66

    def getAndAnalyzeSpeech(self):
        input_text = self.stt.speechToText()

        ta = TextAnalysis(input_text)
        result = ta.analysis()

        formatted_analysis = dict()
        for key in result:
            sentiment = result[key][0]
            words = result[key][1]
            increment = 0
            if sentiment <= self.sadThreshold:
                increment = -1
            elif sentiment >= self.happyThreshold:
                increment = 1
            for word in words:
                formatted_analysis[word] += increment
        







