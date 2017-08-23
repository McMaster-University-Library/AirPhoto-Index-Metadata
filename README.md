# McMaster University's Air Photo Index

** This repository is a resource to create an Air Photo Index presented as an online interactive map. Additional features to this map include historic fire insurance plans, orthoimagery, topographical maps, and a tutorial modal. Access the current Air Photo Index [here.](file:///C:/Home/Air-Photo-Index/AirPhoto-Index-Metadata/AirPhotoIndex/index.html)**

## Folder: AirPhotoIndex

### Resource: Master.tsv

This TSV file is the latest downloaded version of the Google [Master Spreadsheet](https://docs.google.com/spreadsheets/d/180qQStP5EkeY_3a4eM5lXcDYv3QY4zFq4l5bx3BZ8m0/edit#gid=0) that stores all information for McMaster University’s Air Photo Collection to by appropriate Python scripts for Metadata and Air Photo Index creation.

### Tool: Create-API.py

Using Python 2.7.12, this script converts information from the master spreadsheet of aerial photo index metadata in TSV format into HTML format. In addition to base layer maps and markers for each aerial photo in the database, the HTML file created with this script includes layers of historic fire insurance plans, orthoimagery, and topographical maps. A tutorial modal that pops up upon opening the web-page is also included in the HTML file. Majority of the website's functionality is used with Leaflet (Version 0.7.3), an open-source JavaScript library for mobile-friendly interactive maps. All JavaScript and CSS files used for this script are contained within the same folder. Full descriptions for the script's functionality is found within it. Create-API.py was last updated in August 2017 and the Air Photo Index web-page has since been named the Historical Hamilton Portal.

### Folder: Compression

This folder contains a script to compress TIF and XML files in a given directory into ZIP files of smaller sizes. These ZIP files are those that are then batch ingested into the Digital Archive.

### Folder: Metadata

This folder contains a script to generate a tab delimited TXT file containing selected metadata for all sets of aerial photographs from Master.tsv.

### Folder: Thumbnails

This folder contains a script to create thumbnails of original aerial photos using the ImageMagick program.

### _Find the complete user guide in the Google Doc [here.](https://docs.google.com/document/d/15C5t9oEDk808uXAyx8PzxzmvWaYHMnQU5fdk2MuaDOA/edit?usp=sharing)_

### _Student Contributors_

| Student | GitHub Profile |
| --- | --- |
| Victoria Tweedie | [vtweedie](https://github.com/vtweedie) |
| Nick Luymes | [nickluymes](https://github.com/nickluymes) |
| Jordan Aharoni | [jordanaharoni](https://github.com/jordanaharoni) |
| Noel Cochon | [cochonnk](https://github.com/cochonnk) |
| Kayla Wong | --- |
