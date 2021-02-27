import os, json

class Config:
	def __init__(self, filepath):
		self.filepath = filepath

	def get(self):
		if os.path.isfile(self.filepath):
			with open(self.filepath, "r") as config:
				return json.loads(config.read())
		else:
			return None