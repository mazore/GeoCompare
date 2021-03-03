import json
from models.parser import Parser

class Json(Parser):

	@classmethod
	def parse(self, string):
		return geojson.loads(string)

	@classmethod
	def get_location(self, data, key):
		raise NotImplementedError()
	
	@classmethod
	def find_nearby_location(self, lat, long):
		raise NotImplementedError()
