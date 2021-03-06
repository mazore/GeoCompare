# this class is intended as a standardized internal representation of a vaccination location so actions have a standard format that they can use
class VaccinationLocation:
	def __init__(self, name, id, address, lat, lon, source=None):
		self.name = name
		self.id = id
		self.address = address
		self.lat = lat
		self.long = lon
		self.source = source

	@classmethod
	def from_mapped_data(cls, data, datamap, source=None):
		return cls(
			datamap.get_standard_key_from_data("name"),
			datamap.get_standard_key_from_data("id"),
			datamap.get_standard_key_from_data("address"),
			datamap.get_standard_key_from_data("lat"),
			datamap.get_standard_key_from_data("long"),
			source=source
		)

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