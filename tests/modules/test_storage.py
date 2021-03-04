import unittest
from models.storage import CacheEntry
from pathlib import Path
import datetime
import json
from unittest.mock import patch

class TestStorageMethods(unittest.TestCase):
	def setUp(self):
		self.cache = CacheEntry(Path("/some/location"), "myfile.txt", last_saved=datetime.datetime(2021,3,3,11,3,50), mkdir=False)

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

	def test_init_and_getters(self):
		with patch.object(Path, 'mkdir') as mk:
			cache = CacheEntry(Path("/some/location"), "myfile.txt", last_saved=datetime.datetime(2021,3,3,11,3,50))
			# assert that the directory is successfully created
			mk.assert_called_with(parents=True, exist_ok=True)
		
		self.assertEqual(cache.get_date_saved().time(), datetime.datetime(2021,3,3,11,3,50).time())
		self.assertTrue(cache.get_full_path().name.endswith("myfile.txt"))


	def test_age_at_datetime(self):
		self.assertEqual(datetime.timedelta(0), self.cache.get_age_at_datetime(datetime.datetime(2021,3,3,11,3,50)))
		self.assertEqual(datetime.timedelta(seconds=5), self.cache.get_age_at_datetime(datetime.datetime(2021,3,3,11,3,55)))
		self.assertEqual(datetime.timedelta(seconds=-5), self.cache.get_age_at_datetime(datetime.datetime(2021,3,3,11,3,45)))



if __name__ == '__main__':
	unittest.main()