# Fetches GeoJSON from a featureServer URL

# Step 2: append ?f=pjson and parse for the `serviceItemId` value. also check `supportedQueryFormats` for `geoJSON`. possibly also save the name and id of this layer and increment the /0 to get more if any
#Step 3: fetch geoJSON data and store in cache folder (or somewhere, probably not memory). repeat and increment the _0 (layer id) at the end until you get a 400 bad request
# https://opendata.arcgis.com/datasets/{serviceItemId}_{layerID}.geojson


# it might be better to turn this into a simple file-fetcher since these are just json files and need no special sauce to access

import models.fetcher
import requests

class Arcgis(Fetcher):
	def __init__(self, url):
		super(url, "arcgis")

	def auth(self):
		pass

	def fetch(self):
		response = requests.get(self.url)
		if response.status_code == 200:
			with open('response.txt', 'w') as outfile:
   				json.dump(response, outfile)
