from map import Map

class Source:
	def __init__(self, id, name, fetcher_name, url, map, parameters={}):
		self.url = url
		self.name = name
		self.fetcher_name = fetcher_name
		self.id = id
		self.parameters = parameters
		self.map = Map(map)

	@classmethod
	def fromDict(cls, data):
		try:
			params = data["parameters"]
		except KeyError:
			params = {}

		return cls(data['id'], data['name'], data['fetcher'], data['url'], data['map'], parameters=params)

	def fetch(self):
		raise NotImplementedError()

	def get_fetcher_name(self):
		return self.fetcher_name

	def get_name(self):
		return self.name

	def get_url(self):
		return self.url
	
	def get_parameter(self, key):
		try:
			return self.parameters[key]
		except KeyError:
			return None
	
	def get_id(self):
		return self.id

	def get_map(self):
		return self.map
