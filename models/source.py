from map import Map

from parsers.geojson import Geojson
from parsers.csv import Csv
from parsers.json import Json

class Source:
	def __init__(self, id, name, fetcher_name, parser_name, urls, map, parameters={}):
		self.urls = urls
		self.name = name
		self.fetcher_name = fetcher_name
		self.parser_name = parser_name
		self.id = id
		self.parameters = parameters
		self.map = Map(map)

	@classmethod
	def fromDict(cls, data):
		params = data.get("parameters", {})

		return cls(data['id'], data['name'], data['fetcher'], data['parser'],data['url'], data['map'], parameters=params)

	def fetch(self):
		raise NotImplementedError()

	def get_fetcher_name(self):
		return self.fetcher_name
	
	def get_parser_name(self):
		return self.parser_name

	def get_fetcher(self):
		pname = self.get_parser_name()
		if pname == 'csv':
			return Csv()
		elif pname == 'geojson':
			return Geojson()
		elif pname = 'json':
			return Json()

		return None

	def get_name(self):
		return self.name

	def get_url_objects(self):
		return self.urls
	
	def get_parameter(self, key):
		try:
			return self.parameters[key]
		except KeyError:
			return None
	
	def get_id(self):
		return self.id

	def get_map(self):
		return self.map
