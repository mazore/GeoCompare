from pathlib import Path
import datetime
from constants import DATE_FORMAT_STRING

class CacheEntry:
	def __init__(self, location, filename):
		self.location = location
		self.filename = filename

	def get_file_date(self):
		datestr = self.filename.split("_", 1)[0]
		return datetime.datetime.strptime(datestr, DATE_FORMAT_STRING)

	def get_age_since_datetime(self, datetime=datetime.datetime.now()):
		return datetime - self.get_file_date()

	def is_older_than(self, datetime):
		cache = self.get_age_since_datetime(datetime=datetime).total_seconds()
		if cache >= 0:
			return False
		else:
			return True

	def write(self, data):
		writetime = datetime.datetime.now().strftime(DATE_FORMAT_STRING)
		filepath = self.location.joinpath(writetime + "_" + self.filename)
		filepath.write_text(data)
		
