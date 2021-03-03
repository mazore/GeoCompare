from models.storage import CacheEntry
import requests
import json

def get_distance(x1, y1, x2, y2):
	return sqrt((y2-y1)^2+(x2-x1)^2)

def fetch_unless_cache(cachepath, url, filename, headers, force_fetch=False):
	cache_location = CacheEntry.latest_from_directory(cachepath, pattern="*"+filename)
	# if there is no existing cache, create one
	if not cache_location:
		cache_location = CacheEntry(cachepath, filename)

	if not cache_location.exists() or force_fetch:
		response = requests.get(url, headers=headers)

		if response.status_code == 200:
			cache_location.write(response.content, raw=True)
