class Parser:
	def __init__(self, data):
		self.data = data

	@classmethod
	def get_location(self, data, key):
		raise NotImplementedError()
	
	@classmethod
	def find_nearby_location(self, data, lat, long):
		raise NotImplementedError()

	def 

