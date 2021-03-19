# GeoCompare Overview

GeoCompare is intended to be modular in order to a accomodate multiple different formats (both for input and output) of geographic data

## GeoCompare Design

In order to allow GeoCompare to become potentially useful to other projects, the goal is to build it in a fairly modular way such so that its easy to support a new format by adding a new parser and output for the new format. 

![Diagram of GeoCompare Architecture](img/GeoCompare-architecture.png)

## Fetchers
Fetchers save data from sources like API's to a local cache for processing

the fetcher for the most part is just a straight up generic file downloader that pretty much just downloads files to the cache directory. fetchers are mainly to like poke all the right settings in terms of like headers and auth to get the data  downloaded. the parser part is what is meant to actually interperet the files

## Parsers
Parsers are written to provide a somewhat standard set of methods for accessing data from a particular type of file stored in the cache. This abstracts away the need to handle parsing different formats like GeoJSON in other parts of the program

## Actions
Actions perform the actual operations on the data, such as associating records based on the proximity of their coordinates, or checking which records are contained in another dataset in the cache

## Outputs
Outputs are responsible for taking the results of actions and formatting them in th desired format.  This can be used to export the results in formats like CSV, a database, etc.