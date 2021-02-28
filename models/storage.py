from pathlib import Path
import datetime
from constants import DATE_FORMAT_STRING

class CacheEntry:
	def __init__(self, location, filename, last_saved=None delimiter="_"):
		self.location = location
		self.filename = filename
		self.delimiter = delimiter
		self.last_saved = last_saved

	def get_date_saved(self):
		return self.last_saved

	def get_age_at_datetime(self, datetime=datetime.datetime.now()):
		return datetime - self.last_saved

	def is_older_than(self, datetime):
		cache = self.get_age_since_datetime(datetime=datetime).total_seconds()
		if cache >= 0:
			return False
		else:
			return True

	def write(self, data):
		writetime = datetime.datetime.now()
		formatted_writetime = writetime.strftime(DATE_FORMAT_STRING)
		filepath = self.location.joinpath(formatted_writetime + "_" + self.filename)
		filepath.write_text(data)
		self.last_saved = writetime

	def read(self):
		formatted_time = self.last_saved.strftime(DATE_FORMAT_STRING)
		filepath = self.location.joinpath(formatted_time + "_" + self.filename)
		return filepath.read_text(data)
		
