import unittest
from models.config import Config
from models.source import Source
import json


class TestConfigMethods(unittest.TestCase):

	testconfigFile = """{
		"sources": [
			{
				"id": "id",
				"name": "name",
				"parser": "parser",
				"fetcher": "fetcher",
				"urls": [],
				"map": {},
				"parameters": {
					"test": "true"
				}
			}
		],
		"actions": []
	}"""

	def test_get_sources(self):
		srcs = [Source("id", "name", "fetcher", "parser", [], {}, parameters={"test": "true"})]
		inited = Config(sources=srcs)
		self.assertEqual(inited.get_sources(), srcs)


	def test_from_dict(self):
		test_dict = json.loads(TestConfigMethods.testconfigFile)
		conf = Config.from_dict(test_dict)
		self.assertEqual(len(conf.get_sources()), 1)
		self.assertEqual(conf.get_sources()[0].get_fetcher_name(), "fetcher")

if __name__ == '__main__':
	unittest.main()