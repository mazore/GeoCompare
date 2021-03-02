# Fetches GeoJSON from a featureServer URL

# Step 2: append ?f=pjson and parse for the `serviceItemId` value. also check `supportedQueryFormats` for `geoJSON`. possibly also save the name and id of this layer and increment the /0 to get more if any
#Step 3: fetch geoJSON data and store in cache folder (or somewhere, probably not memory). repeat and increment the _0 (layer id) at the end until you get a 400 bad request
# https://opendata.arcgis.com/datasets/{serviceItemId}_{layerID}.geojson


# it might be better to turn this into a simple file-fetcher since these are just json files and need no special sauce to access

# Data for FL and CO to use for smaller-scale testing to see what benefits this might bring for either side

# CO:
# https://docs.google.com/spreadsheets/d/1124pvazfFxhHkfFldcdrhSoh8DlpPwu0QvUskupEiG0/gviz/tq?tqx=out:csv&sheet=CO
# same thing for FL, just... with FL instead of CO at the end

# from fheisler


from models.fetcher import Fetcher
from models.storage import CacheEntry
from helpers import make_cached_request
import requests

class Googledrive(Fetcher):
	def __init__(self):
		super().__init__("googledrive")
		# designate a folder inside the cache for this fetchers files
		self.cachepath = self.cachepath.joinpath(self.name)

	def build_headers(self):
		return super().build_headers().update({})

	def auth(self):
		pass

	def fetch(self, source):
		sheets = source.get_parameter("sheets")

		if sheets:
			for sheet in sheets:
				self.fetch_as_csv(source.get_url(), source.get_name(), sheet=sheet)
		else:
			self.fetch_as_csv(source.get_url(), source.get_name())

	def fetch_as_csv(self, url, filetitle, sheet=None, force_fetch=None):
		filename = self.generate_cachefile_name(filetitle, sheet=sheet)
		url = self.generate_drive_csv_url(url, sheet=sheet)	
		return make_cached_request(self.cachepath, url, filename, self.build_headers(), force_fetch=force_fetch)

	def generate_cachefile_name(self, name, sheet=None):
		if sheet:
			name += "-" + sheet
		
		name += ".csv"
		return name

	def generate_drive_csv_url(self, url, sheet=None):
		finalurl = url + "/gviz/tq?tqx=out:csv"
		if sheet:
			finalurl += "&sheet={sheet}".format(sheet=sheet)
		return finalurl
