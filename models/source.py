class Source:
	def __init__(self, id, name, fetcher_name, url):
		self.url = url
		self.name = name
		self.fetcher_name = fetcher_name
		self.id = id

	@classmethod
	def fromDict(cls, data):
		return cls(data['id'], data['name'], data['fetcher'], data['url'])

	def fetch(self):
		raise NotImplementedError()

	def get_fetcher_name(self):
		return self.fetcher_name

	def get_url(self):
		return self.url
	
	def get_id(self):
		return self.id

