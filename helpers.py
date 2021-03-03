from models.storage import CacheEntry
import requests
import json

def get_distance(x1, y1, x2, y2):
	return sqrt((y2-y1)^2+(x2-x1)^2)

def make_cached_request(cachepath, url, filename, headers, force_fetch=False):
	cache_location = CacheEntry.latest_from_directory(cachepath)
	if cache_location.exists() and not force_fetch:
		data = json.loads(cache_location.read())
	else:
		response = requests.get(url, headers=headers)

		if response.status_code == 200:
			data = response.content.decode()
			cache_location.write(data)
	return data