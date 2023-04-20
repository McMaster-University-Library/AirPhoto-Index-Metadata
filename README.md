# McMaster University's Air Photo Index

**This repository is a resource to create an Air Photo Index presented as an online interactive map. Additional features to this map include historic fire insurance plans, orthoimagery, topographical maps, aerial photo envelopes, and a tutorial modal. Access the current Air Photo Index [here.](http://library.mcmaster.ca/maps/aerialphotos/index.html)**

## Change History

### 2020-11-02 (JJB)
- Updated path to tiles (FIPs, Orthos, Topos)
- For FIPs, changed reference in Create-API.py from ```http://perec.mcmaster.ca/maps``` to ```https://library.mcmaster.ca/tiles/```
- For Orthos, changed reference in Create-API.py from ```http://tiles.mcmaster.ca``` to ```https://library.mcmaster.ca/tiles/```
- For Topos, changed all references in ```index_body_topography.txt``` from ```http://perec.mcmaster.ca/maps``` to ```https://library.mcmaster.ca/tiles/```
- Updated links to FIP collection information in ```index_body_fire.txt```

## Process for adding more photos to the Air Photo Index
1. Scan the images with the feed-through scanner
- Find a good spot on the scanner to feed in images -- hitting two rollers
- Follow the established naming convention for the images
- [Internal scanning intstructions](https://docs.google.com/document/d/1BbmKHinXS_xmfCYKsvTkttX6oUojLWhQc5AQQo2W13U/edit)
2. Create metadata files
- [Christine] Copy metadata from [Aerial Photo Master List](https://docs.google.com/spreadsheets/d/180qQStP5EkeY_3a4eM5lXcDYv3QY4zFq4l5bx3BZ8m0/edit#gid=0) to a new tab on the [Bulk metadata template google sheet](https://docs.google.com/spreadsheets/d/1xmSuWdqUQ0a9RNCi2DErNO1bBcK6J06ps0moyYkg4Qk/edit#gid=1991707764) 
- More info here: https://github.com/McMaster-University-Library/Digital-Archive-Tools/tree/master/BulkTools
3. [Jay] Bulk ingest
- Suggest we try zipping and using the built-in bulk ingester (Jay)
4. [Jay] Update Aerial Photo Master sheet
- Digital Archive URL (via updating the DigArc-Id2URL-ToMerge tab)
5. (one time only) Add accessibility items
- Review changes made to index.html; make related changes to Create-API.py and all .txt files in the top-level directory
6. Export the Master Sheet; process with python script 
7. Copy the index.html file to the test server -- more information [here](https://github.com/McMaster-University-Library/gis-data-reference-documents/blob/main/lists.md#list-of-map-indexes). 
8. Confirm the changes are applied as expected and no other issues exist.
7. Copy index.html file to the production server.


## Folder: AirPhotoIndex

### Resource: Master.tsv

This TSV file is the latest downloaded version of the Google [Master Spreadsheet](https://docs.google.com/spreadsheets/d/180qQStP5EkeY_3a4eM5lXcDYv3QY4zFq4l5bx3BZ8m0/edit#gid=0) that stores all information for McMaster University’s Air Photo Collection using appropriate Python scripts for Metadata and Air Photo Index creation.

### Tool: Create-API.py

Using Python 2.7.12, this script converts information from the master spreadsheet of aerial photo index metadata in TSV format into HTML format. In addition to base layer maps and markers for each aerial photo in the database, the HTML file created with this script includes layers of historic fire insurance plans, orthoimagery, topographical maps, and aerial photo envelopes. A tutorial modal that pops up upon opening the web-page is also included in the HTML file. Majority of the website's functionality is used with Leaflet (Version 1.4.0), an open-source JavaScript library for mobile-friendly interactive maps. All JavaScript and CSS files used for this script are contained within the same folder. Full descriptions for the script's functionality is found within it. Create-API.py was last updated in March 2018 and the Air Photo Index web-page has since been named the Historical Hamilton Portal.

The following steps are a quick guide in using Create-API.py to create or update the existing Air Photo Index web-page.

	1. Download the latest version of the Google Master Spreadsheet as a TSV file.
	2. Rename it Master.tsv, and place it in the same folder or directory as the Create-API.py.
	3. Run Create-API.py by right clicking the script, opening it in IDLE, and hitting F5 once the program is open.
	4. The Air Photo Index will be created in an HTML document, named index.html, within the same directory as the Create-API.py script that was run. 

### Resource: index.html

This HTML file presents the Air Photo Index as an online interactive map, with additional features including historic fire insurance plans, orthoimagery, topographical maps, aerial photo envelopes, and a tutorial modal. This file is created by running the Python script Create-API.py, along with the Leaflet library for mobile-friendly interactive maps. All JavaScript and CSS files used within the HTML document are contained within the same folder. The latest version of index.html can be found online [here,](http://library.mcmaster.ca/maps/aerialphotos/index.html) through the McMaster University Library website.
	
## Folder: Compression

This folder contains a script to compress TIF and XML files in a given directory into ZIP files of smaller sizes. These ZIP files are those that are then batch ingested into the Digital Archive.

## Folder: Metadata

This folder contains a script to generate a tab delimited TXT file containing selected metadata for all sets of aerial photographs from Master.tsv.

## Folder: Thumbnails

This folder contains a script to create thumbnails of original aerial photos using the ImageMagick program.

### _McMaster University Library Student Contributors_

| Student | GitHub Profile |
| --- | --- |
| Victoria Tweedie | [vtweedie](https://github.com/vtweedie) |
| Nick Luymes | [nickluymes](https://github.com/nickluymes) |
| Jordan Aharoni | [jordanaharoni](https://github.com/jordanaharoni) |
| Noel Cochon | [cochonnk](https://github.com/cochonnk) |
| Kayla Wong |    |

### _Find the complete user guide and project documentation in the Google Doc [here.](https://docs.google.com/document/d/15C5t9oEDk808uXAyx8PzxzmvWaYHMnQU5fdk2MuaDOA/edit?usp=sharing)_
