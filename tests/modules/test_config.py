import unittest
from models.config import Config
from models.source import Source
from unittest.mock import patch, mock_open



class TestConfigMethods(unittest.TestCase):

	testconfigFile = """{
		"sources": [
			{
				"name": "name",
				"fetcher": "fetcher",
				"url": "url"
			}
		]
	}"""

	def test_get_sources(self):
		srcs = [Source("name", "fetcher", "url")]
		inited = Config(sources=srcs)
		self.assertEqual(inited.get_sources(), srcs)


	def test_from_dict(self):
		test_dict = json.parse(TestConfigMethods.testconfigFile)
		conf = Config.from_dict(test_dict)
		self.assertEqual(len(conf.get_sources()), 1)
		self.assertEqual(conf.get_sources()[0].get_fetcher_name(), "fetcher")

if __name__ == '__main__':
	unittest.main()