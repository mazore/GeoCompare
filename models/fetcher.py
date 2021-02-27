import datetime
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

	def build_headers(self):
		return { 'User-Agent': self.useragent }
	
	def get_cachepath(self):
		return self.cachepath

	def should_fetch(self):
		raise NotImplementedError()
	
	def get_filename(self, extension="txt"):
		return self.get_cachepath() + datetime.datetime.now().strftime('%Y-%m-%dT%H%M%S') + "." + extension

	def auth(self):
		raise NotImplementedError()

	def fetch(self):
		raise NotImplementedError()