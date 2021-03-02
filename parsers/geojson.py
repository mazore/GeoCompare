# Provide methods that can be used by other parts of this program to access 

import geojson
from models.parser import Parser

class Geojson(Parser):

	@classmethod
	def parse(self, string):
		return geojson.loads(string)

	@classmethod
	def get_location(self, data, key):
		# GlobalID
		raise NotImplementedError()
	
	@classmethod
	def find_nearby_location(self, lat, long):
		raise NotImplementedError()


# with open(path_to_file) as f:
#     gj = geojson.load(f)
# features = gj['features'][0]