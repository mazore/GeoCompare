class Source:
	def __init__(self, name, fetcher_name, url, id=None):
		self.url = url
		self.name = name
		self.fetcher_name = fetcher_name
		self.id = id

	@classmethod
	def fromDict(cls, data):
		try:
			identifier = data["id"]
		except KeyError:
			identifier=None
		return cls(data['name'], data['fetcher'], data['url'], id=identifier)

	def fetch(self):
		raise NotImplementedError()

	def get_fetcher_name(self):
		return self.fetcher_name

	def get_url(self):
		return self.url
	
	def get_id(self):
		return self.id

	def set_id(self, id):
		self.id = id
