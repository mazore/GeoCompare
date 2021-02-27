import os

class Fetcher:
	def __init__(self, url, name, cachepath=None):
		self.url = url
		self.name = name
		self.useragent = "GeoCompare script (https://github.com/VacFind/GeoCompare)"

		if (cachepath):
			self.cachepath = cachepath
		else:
			self.cachepath = os.getcwd() + "/cache"

	def auth(self):
		raise NotImplementedError()

	def fetch(self):
		raise NotImplementedError()