# Backstory
GeoCompare came about primarily as the result of two similar ideas.

1. GISCorps maintains a few [map layers](https://covid-19-giscorps.hub.arcgis.com/) with national COVID data (primarily  vaccination and testing site locations). [Many states](https://docs.google.com/spreadsheets/d/11rbU89mdvYEPnKNKVOluUlgjw5n9qkrSFmHenkjZtfU/edit#gid=0) also seem to also use the same platform as GISCorps (that platform being ArcGIS, made by Esri) to host their own maps of vaccination sites. Some of these state level maps have more or different sites than the GISCorps data and after looking into it, it turns out that the built-in tools for importing data between these datasets trhough the ArcGIS platform basically will replace the current data in the GISCorps dataset with the new one rather than merging them. This would mean all of  GISCorps' custom fields for COVID-related info would need to be re-done. 

2. Associate the vaccination locations from the databases of projects like findyourvaccine.org and compare it against the locations in the GISCorps natopnal dataset to see if one dataset has locations the other does not.


So the general premise of GeoCompare is to enable different datasets containing geographic locations to compare/process and otherwise exchange their data in useful ways.