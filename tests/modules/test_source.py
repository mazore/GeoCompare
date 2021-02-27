import unittest
from models.source import Source

class TestSourceMethods(unittest.TestCase):

	def test_from_dict(self):
		reg = Source("name", "fetcher", "https://foo.com")
		dictionary = Source.fromDict({
			"name": "name",
			"fetcher": "fetcher",
			"url": "https://foo.com"
		})
		self.assertEqual(reg.name, dictionary.name)
		self.assertEqual(reg.fetcher_name, dictionary.fetcher_name)
		self.assertEqual(reg.url, dictionary.url)

if __name__ == '__main__':
	unittest.main()