# This class provides an easier means of interacting with the `map` subtype within sources to map keys from the source to a standard internal datatype for processing

class Map:
	def __init__(self, mapdata, name=None):
		self.name = name
		self.mapdata = mapdata

	def get_name(self):
		return self.name

	def get_standard_key_from_data(self, std_key, nsdata):
		# get nonstandard key for the nonstandard data
		ns_key = self.mapdata[std_key]
		return nsdata[ns_key]
	
	

	