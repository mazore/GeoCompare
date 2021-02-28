import datetime
import os
from pathlib import Path
from constants import USER_AGENT_STRING


class Fetcher:
	def __init__(self, name, cachepath="./cache"):
		self.name = name
		self.useragent = USER_AGENT_STRING
		self.cachepath = Path(cachepath)

	def build_headers(self):
		return { 'User-Agent': self.useragent }
	
	def get_cachepath(self):
		return self.cachepath

	def should_fetch(self):
		raise NotImplementedError()

	def auth(self):
		raise NotImplementedError()

	def fetch(self, source):
		raise NotImplementedError()