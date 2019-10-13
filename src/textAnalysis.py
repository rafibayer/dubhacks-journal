'''
https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python

USAGE:
Create new TextAnalysis instance: ta = TextAnalysis(input_texts)

use azure text analytics to return sentiments of sentences and key associated entities

results = ta.analysis()

results is formatted as a dictionary: results[id] = (sentiment score from 0-1, [list of key words])
example: {0: (0.0024226605892181396, ['Rome']), 1: (0.024681180715560913, ['$200'])}
'''

import requests
import os
import json
from pprint import pprint

class TextAnalysis():
    def __init__(self, input_texts):
        self.documents = {"documents":[]}
        temp_dict = dict()
        for idx, input_text in enumerate(input_texts):
            temp_dict['id'] = idx+1
            temp_dict['language'] = "en"
            temp_dict['text'] = input_text
            self.documents['documents'].append(temp_dict.copy())
            temp_dict.clear()
        
        # self.documents = {"documents": [
        #     {"id": "1", "language": "en",
        #         "text": "I miss Rome"},
        #     {"id": "2", "language": "en",
        #         "text": "I'm having some money issues. Nothing too big, but I can't afford $200."}
        # ]}

    def analysis(self):
        key_var_name = 'TEXT_ANALYTICS_SUBSCRIPTION_KEY'
        #if not key_var_name in os.environ:
        #    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
        #subscription_key = os.environ[key_var_name]
        subscription_key = "b136f99ab8f445f4982b717a07d301d3"

        endpoint_var_name = 'TEXT_ANALYTICS_ENDPOINT'
        #if not endpoint_var_name in os.environ:
        #    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
        #endpoint = os.environ[endpoint_var_name]
        endpoint = "https://emotionapptextanalysis.cognitiveservices.azure.com/"

        sentiment_url = endpoint + "/text/analytics/v2.1/sentiment"

        #documents = self.documents
        print(self.documents)

        #hit azure for sentiment analysis
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(sentiment_url, headers=headers, json=self.documents)
        sentiments = response.text
        #pprint(sentiments)
        
        sentiments_response = json.loads(sentiments)

        entities_url = endpoint + "/text/analytics/v2.1/entities"

        #hit azure for entity extraction
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(entities_url, headers=headers, json=self.documents)
        entities = response.text
        #pprint(entities)

        entities_response = json.loads(entities)

        scores = dict()
        sentiment_scores_dict = dict()
        entity_dict = dict()
        text_analysis = dict()
        number_of_ids = len(sentiments_response['documents'])

        for i in range(number_of_ids):
            scores[i] = sentiments_response['documents'][i]['score']
            number_of_entities = len(entities_response['documents'][i]['entities'])
            entities_text_list = []
            for j in range(number_of_entities):
                entity_type = entities_response['documents'][i]['entities'][j]['type']
                if entity_type == "Person" or entity_type == "Location" or entity_type == "Organization" or\
                    entity_type == "Age" or entity_type == "Quantity":
                    entities_text_list.append(entities_response['documents'][i]['entities'][j]['matches'][0]['text'])
            
            entity_dict[i] = entities_text_list

        for i in range(number_of_ids):
            text_analysis[i] = (scores[i], entity_dict[i])
        
        return text_analysis