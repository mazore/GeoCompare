import os, json
from pathlib import Path
from models.source import Source

class Config:
	def __init__(self, sources=[]):
		self.sources = sources


	@classmethod
	def from_file(cls, filename):
		path = Path(filename)
		data = json.loads(path.read_text())
		return cls.from_dict(data)

	@classmethod
	def from_dict(cls, data):
		sources = []
		for source in data["sources"]:
			sources.append(Source.fromDict(source))
		
		return cls(sources=sources)


	def get_sources(self):
		return self.sources