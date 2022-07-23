from auth import *
import requests

model = "cardiffnlp/twitter-roberta-base-sentiment-latest"
API_URL = "https://api-inference.huggingface.co/models/" + model

class sentAnalModel:
 	"""
	HuggingFace model to run analysis on tweets
 	"""
 	def __init__(self):
 		self.API_URL = API_URL
 		self.headers = {"Authorization": "Bearer %s" % (hf_token)}
 	def analysis(self, data):
 		payload = dict(inputs=data, options=dict(wait_for_model=True))
 		response = requests.post(self.API_URL, headers=self.headers, json=payload)
 		return response.json()