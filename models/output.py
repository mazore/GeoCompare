class Output:
	def __init__(self, path):
		self.path = path

	def write(self):
		raise NotImplementedError()