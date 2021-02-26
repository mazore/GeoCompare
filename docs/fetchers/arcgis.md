# ArcGIS Fetcher

ArcGIS is a very common tool for displaying Geographic data (such as vaccination and testing sites for COVID).

Data is available in "Feature layers" that can be added to existing maps using libraries like leafletjs, or in case of this script, parsed as geoJSON.

It seems as though all states that use ArcGIS has publicly-accessible API's for accessing these feature layers. These endpoints and some documentation can be found by looking for requests to domains similar to `services.arcgis.com` and finding the links that end in `/FeatureServer/#` where # is the layer ID.

The ArcGIS fetcher should fetch and store this geoJSON data for further processing by the parsers