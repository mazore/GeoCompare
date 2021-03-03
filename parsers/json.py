import json
from models.parser import Parser

class Json(Parser):
	def __init__(self, data):
		super().__init__(json.loads(data))

	@classmethod
	def get_location(self, data, key):
		raise NotImplementedError()
	
	@classmethod
	def find_nearby_location(self, lat, long):
		raise NotImplementedError()
