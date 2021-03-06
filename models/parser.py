class Parser:
	def __init__(self, keymap):
		self.keymap = keymap

	@classmethod
	def get_location(self, data, key):
		raise NotImplementedError()
	
	@classmethod
	def find_nearby_location(self, data, lat, long):
		raise NotImplementedError()

	def 

