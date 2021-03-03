import unittest
from models.storage import CacheEntry
from pathlib import Path
import datetime
import json
from unittest.mock import patch

class TestStorageMethods(unittest.TestCase):

	def test_make_cache_entry_from_filename(self):
		filename = "2020-02-02T020202_myfile.txt" 
		with patch.object(Path, 'is_file', return_value=True) as ex:
			cacheentry = CacheEntry.from_filename(filename)
			ex.assert_called_with()
		self.assertEqual(cacheentry.get_date_saved().time(), datetime.datetime(year=2020, month=2, day=2, hour=2, minute=2, second=2).time())
		self.assertEqual(cacheentry.filename, "myfile.txt")

	def test_make_cache_entry_from_nonexistent_filename(self):
		filename = "2020-02-02T020202_myfile.txt" 
		with self.assertRaises(ValueError) as context:
			cacheentry = CacheEntry.from_filename(filename)
		

if __name__ == '__main__':
	unittest.main()