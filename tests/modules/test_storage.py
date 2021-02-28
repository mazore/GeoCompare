import unittest
from models.storage import CacheEntry
import datetime
import json

class TestStorageMethods(unittest.TestCase):

	def test_make_cache_entry_from_filename(self):
		filename = "2020-02-02T020202_myfile.txt" 
		cacheentry = CacheEntry.from_filename(filename)
		self.assertEqual(cacheentry.get_date_saved().time(), datetime.datetime(year=2020, month=2, day=2, hour=2, minute=2, second=2).time())
		self.assertEqual(cacheentry.filename, "myfile.txt")


if __name__ == '__main__':
	unittest.main()