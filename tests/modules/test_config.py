import unittest
from models.config import Config
from unittest.mock import patch, mock_open



class TestConfigMethods(unittest.TestCase):

	testconfigFile = """{
		"sources": [
			{
				"name": "giscorps-vaccination-sites",
				"fetcher": "arcgis",
				"url": "https://services.arcgis.com/8ZpVMShClf8U8dae/arcgis/rest/services/Covid19_Vaccination_Locations/FeatureServer/0"

			}
		]
	}"""

	def test_init(self):
		inited = Config("./some_file")
		self.assertEqual(inited.filepath, "./some_file")

	# https://stackoverflow.com/a/34677735
	@patch("builtins.open", new_callable=mock_open, read_data=testconfigFile)
	@patch("os.path")
	def test_get(self, mock_path, mock_file):
		# set up the mock
		mock_path.isfile.return_value = True
		inited = Config("./some_file")
		config = inited.get()
		mock_file.assert_called_with("./some_file", "r")
		mock_path.isfile.assert_called_with("./some_file")
		# TODO: assertions about contents of config

if __name__ == '__main__':
	unittest.main()