class VaccinationLocation:
	def __init__(self, name, id, address, lat, lon, source=None):
		self.name = name
		self.id = id
		self.address = address
		self.lat = lat
		self.long = lon
		self.source = source

	def get_name(self):
		return self.name
	
	def get_address(self):
		return self.address

	def get_id(self):
		return self.id

	def get_lat(self):
		return self.lat

	def get_long(self):
		return self.long

	def get_source(self):
		return self.source