# Fetches GeoJSON from a featureServer URL

# Step 2: append ?f=pjson and parse for the `serviceItemId` value. also check `supportedQueryFormats` for `geoJSON`. possibly also save the name and id of this layer and increment the /0 to get more if any
#Step 3: fetch geoJSON data and store in cache folder (or somewhere, probably not memory). repeat and increment the _0 (layer id) at the end until you get a 400 bad request
# https://opendata.arcgis.com/datasets/{serviceItemId}_{layerID}.geojson


# it might be better to turn this into a simple file-fetcher since these are just json files and need no special sauce to access

from models.fetcher import Fetcher
from models.storage import CacheEntry
import requests
import json

class Arcgis(Fetcher):
	def __init__(self):
		super().__init__("arcgis")
		# designate a folder inside the cache for this fetchers files
		self.cachepath = self.cachepath.joinpath(self.name)

	def build_headers(self):
		return super().build_headers().update({})

	def auth(self):
		pass

	def fetch(self, source):
		response = requests.get(self.url)
		if response.status_code == 200:
			with open('response.txt', 'w') as outfile:
   				json.dump(response, outfile)

	def get_info(self, url, force_fetch=False):
		schema_location = CacheEntry(self.cachepath, "schema.json")
		url = url + "?f=pjson"

		if schema_location.exists() and not force_fetch:
			data = json.loads(schema_location.read())
		else:
			try:
				response = requests.get(url, headers=self.build_headers())	
				# print(vars(response))
				if response.status_code == 200:
					result = response.content.decode()
					schema_location.write(result)
					data = json.loads(result)
			except requests.HTTPError as e:
				print("HTTP error while requesting " + url)

		return data

	def fetch_geojson(self, serviceItemID, layerID):	
		url = self.generate_geojson_url(serviceItemID, layerID=layerID)
		filename = url.split("/")[-1]
		cache_location = CacheEntry(self.cachepath, filename)
		response = requests.get(url, headers=self.build_headers())

		if response.status_code == 200:
			cache_location.write(response.content)

	def generate_geojson_url(self, serviceItemID, layerID=0):
		url = "https://opendata.arcgis.com/datasets/{serviceItemId}_{layerID}.geojson"
		return url.format(serviceItemID=serviceItemID, layerID=layerID)
