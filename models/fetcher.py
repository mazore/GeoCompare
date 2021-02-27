class Fetcher:
	def __init__(self, url, name):
		self.url = url
		self.name = name
		self.useragent = ""


	def auth(self):
		raise NotImplementedError()

	def fetch(self):
		raise NotImplementedError()