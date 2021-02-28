import datetime
import os
from pathlib import Path
from constants import USER_AGENT_STRING, DATE_FORMAT_STRING


class Fetcher:
	def __init__(self, url, name, cachepath=None):
		self.url = url
		self.name = name
		self.useragent = USER_AGENT_STRING
		self.cachepath = Path(cachepath)

	def build_headers(self):
		return { 'User-Agent': self.useragent }
	
	def get_cachepath(self):
		return self.cachepath

	def should_fetch(self):
		raise NotImplementedError()
	
	def get_filename(self, extension="txt"):
		return self.get_cachepath() + datetime.datetime.now().strftime(DATE_FORMAT_STRING) + "." + extension

	def auth(self):
		raise NotImplementedError()

	def fetch(self):
		raise NotImplementedError()