import csv
from models.parser import Parser
from models.datatypes.vaccinationlocation import VaccinationLocation

class Csv(Parser):
	def __init__(self, map):
		super().__init__(map)

	@classmethod
	def get_location(self, data, key):

		pass

	@classmethod
	def get_locations(self, data):
		# https://docs.python.org/3/library/csv.html#csv.DictReader
		csvdatadict = csv.DictReader(data)
		return [VaccinationLocation.from_mapped_data(item, self.map) for item in csvdatadict]

	@classmethod
	def find_nearby_location(self, lat, long):
		pass