# McMaster University's Air Photo Index

**This repository is a resource to create an Air Photo Index presented as an online interactive map. Additional features to this map include historic fire insurance plans, orthoimagery, topographical maps, aerial photo envelopes, and a tutorial modal. Access the current Air Photo Index [here.](http://library.mcmaster.ca/maps/aerialphotos/index.html)**

## Folder: AirPhotoIndex

### Resource: Master.tsv

This TSV file is the latest downloaded version of the Google [Master Spreadsheet](https://docs.google.com/spreadsheets/d/180qQStP5EkeY_3a4eM5lXcDYv3QY4zFq4l5bx3BZ8m0/edit#gid=0) that stores all information for McMaster University’s Air Photo Collection using appropriate Python scripts for Metadata and Air Photo Index creation.

### Tool: Create-API.py

Using Python 2.7.12, this script converts information from the master spreadsheet of aerial photo index metadata in TSV format into HTML format. In addition to base layer maps and markers for each aerial photo in the database, the HTML file created with this script includes layers of historic fire insurance plans, orthoimagery, topographical maps, and aerial photo envelopes. A tutorial modal that pops up upon opening the web-page is also included in the HTML file. Majority of the website's functionality is used with Leaflet (Version 0.7.3), an open-source JavaScript library for mobile-friendly interactive maps. All JavaScript and CSS files used for this script are contained within the same folder. Full descriptions for the script's functionality is found within it. Create-API.py was last updated in March 2018 and the Air Photo Index web-page has since been named the Historical Hamilton Portal.

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