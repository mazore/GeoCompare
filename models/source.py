class Source:
	def __init__(self, name, fetcher_name, url):
		self.url = url
		self.name = name
		self.fetcher_name = fetcher_name

	@classmethod
	def fromDict(cls, data):
		return cls(data['name'], data['fetcher'], data['url'])

	def fetch(self):
		raise NotImplementedError()

	def get_fetcher_name(self):
		return self.fetcher_name