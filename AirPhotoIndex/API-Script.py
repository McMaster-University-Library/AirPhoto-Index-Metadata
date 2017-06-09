# -*- coding: cp1252 -*-

# THIS PYTHON SCRIPT CONVERTS INFORMATION FROM THE MASTER SPREADSHEET OF AIR PHOTO INDEX METADATA IN .TSV FORMAT INTO .HTML FORMAT.
# ADDITIONALLY, THE SCRIPT INCLUDES A WELCOME PAGE POP-UP FEATURE THAT IS WRITTEN INTO THE .HTML CODE.

import os
import sys

# SETTING INPUT AND OUTPUT FILES.
inFile = open('Master_Spreadsheet_Current.tsv') #Defining the file located in the directory of this script that stores the information.
outfn = 'index.html' #Defining the desired name of output file.
if os.path.exists(outfn): #Checking if file exists.
    print 'It appears that '+ outfn +' already exists!' 
    os.remove(outfn) #Removing the file if it exists.
    print outfn +' has now been removed!'
else:
    print outfn +' does not already exist!' #This will be written if the file does not exist.
outFile = open(outfn, 'w') #Create a new output File (.html).

# READ TSV FILE.
allcontent = inFile.readlines() #Read tsv and group contents line by line.
content = allcontent[3:] #Remove the first and second line from the content which contain the titles, which we will not include.

# GATHER UNIQUE YEARS FROM 'inFile'.
years = [] #Create an empty array where years from the spreadsheet (.tsv, inFile) will be stored.
for line in content:
    item = line.split('\t') #Split lines of inFile into 'item' at each tab.
    year = item[17]
    if year[0] == '[':
        year = year[1:-1]
    year = year[:4]
    years.append(year) #Adding the first column [0] to the empty array named 'years'.
markerYears = sorted(set(years)) #Getting unique years and sorting them numerically.
markerYears = map(int,markerYears) #This is a list of unique years for all the metadata information.

# WRITING THE HTML CODE'S HEADER. ---------------------------------------------------------------------------------------------------------------
Openhtml = '<html> \n'
outFile.write(Openhtml)

# WRITING THE HEADER SECTION.
headbeginning = """
    <head> 
        <title>McMaster University's Aerial Photographic Index</title>
        <meta charset="utf-8" />
	"""
headwelcome = """
        <!----------THE FOLLOWING IS FOR THE WELCOME PAGE POP-UP.---------->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="initial-scale=1,user-scalable=no,maximum-scale=1,width=device-width">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="style.css">
        <!----------------------------------------------------------------->
        """
headend = """
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />
        <link rel="stylesheet" type="text/css" href="css/own_style.css">
        <link href="http://loopj.github.io/jquery-simple-slider/css/simple-slider.css" rel="stylesheet" type="text/css" />
        <link rel="stylesheet" href="css/API.css">
        <link rel="stylesheet" href="https://ismyrnow.github.io/Leaflet.groupedlayercontrol/src/leaflet.groupedlayercontrol.css">
        <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
        <script src="data/FIP_bounds.js"></script>
        <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
        <script src="https://ismyrnow.github.io/Leaflet.groupedlayercontrol/src/leaflet.groupedlayercontrol.js"></script>
        <script src="js/simple-slider.js"></script>
        <script src="js/control-layers.js"></script>
        <script src="https://api.mapbox.com/mapbox.js/plugins/leaflet-markercluster/v0.4.0/leaflet.markercluster.js"></script>
        <link href="https://api.mapbox.com/mapbox.js/plugins/leaflet-markercluster/v0.4.0/MarkerCluster.css" rel="stylesheet" />
        <link href="https://api.mapbox.com/mapbox.js/plugins/leaflet-markercluster/v0.4.0/MarkerCluster.Default.css" rel="stylesheet" />
        <link rel="stylesheet" href="http://eclipse1979.github.io/leaflet.slider/dist/leaflet-slider.css">
        <script src="http://eclipse1979.github.io/leaflet.slider/dist/leaflet-slider.js"></script>

    </head> 
        """

outFile.write(headbeginning)
outFile.write(headwelcome)
outFile.write(headend)

# WRITING THE HTML'S BODY (INCLUDES THE WELCOME PAGE POP-UP AND THE MAP).
# Width and height can be changed to desired percentage of the frame/browser.
htmlbody="""
<body>

<!-------THE FOLLOWING IS FOR THE WELCOME PAGE POP-UP.--------->

<!-- Trigger/Open The Modal -->
<button id="myBtn"><p>Click Here For a Tutorial on Using the Air Photo Index.</p></button>

<div id="map" style="width: 100%; height: 85%"></div> 
		
<!-- The Modal -->
<div id="myModal" class="modal">

<!-- Modal content -->
	<div class="modal-content">
  
  <!-- Modal header -->
		<div class="modal-header">
		  <span class="close">x</span>
		  <h2>Welcome to the McMaster University Library's Historical Hamilton Portal</h2>
		</div>

		<div class="w3-content w3-display-container">

		<a class="w3-btn-floating w3-hover-dark-grey w3-display-left" onclick="plusDivs(-1)">&#10094;</a>
		<a class="w3-btn-floating w3-hover-dark-grey w3-display-right" onclick="plusDivs(1)">&#10095;</a>
		
		<!-- Slide 1 -->
		<div class="w3-display-container mySlides">
		  <img src="image0.png" style="width:100%">
		  <div class="modal-footer">
			Welcome to the McMaster University Library's Historical Hamilton Portal -- An interactive tool for finding and accessing aerial photos, fire insurance plans and other cartographic materials for the Hamilton area. <br> 
			Close this window (or click on the map) to begin exploring.
		  </div>
		</div>
		
		<!-- Slide 2 -->
		<div class="w3-display-container mySlides">
		  <img src="image1.png" style="width:100%">
		  <div class="modal-footer">
			The center location of each <b>aerial photo</b> in our collection is identified with a marker.
			Explore our collection by navigating the map and using the time slider to select a year of interest.<br>
			Aerial photos in our collection are identified with markers.
		  </div>
		</div>

		<!-- Slide 3 -->
		<div class="w3-display-container mySlides">
		  <img src="image6.png" style="width:100%">
		  <div class="modal-footer">
			Click on a <b>marker</b> to find more information on an aerial photo, including an image preview and a link to a digital version (if available).
		  </div>
		</div>

		<!-- Slide 4 -->
		<div class="w3-display-container mySlides">
		  <img src="image3.png" style="width:100%">
		  <div class="modal-footer">
			Change the <b>base map</b> using the layer panel.
		  </div>
		</div>
		
		<!-- Slide 5 -->
		<div class="w3-display-container mySlides">
		  <img src="image2.png" style="width:100%">
		  <div class="modal-footer">
			Explore a <b>historic fire insurance plan</b> layer by selecting it on the navigation panel.
		  </div>
		</div>

		<!-- Slide 6 -->
		<div class="w3-display-container mySlides">
		  <img src="image4.png" style="width:100%">
		  <div class="modal-footer">
			View a modern orthoimagery layer by selecting it on the navigation panel.<br>
		(Available only to McMaster users)
		  </div>
		</div>
		
		<!-- Slide 7 -->
		<div class="w3-display-container mySlides">
		  <img src="image5.png" style="width:100%">
		  <div class="modal-footer">
			Use the opacity slider to blend layers together. 
		  </div>
		</div>
		
		</div>
		
		<!---Slide changes end.--->
	
	</div>
</div>	

<script src="window.js"></script>

<!---------------------END OF WELCOME PAGE POP-UP.------------------------>

"""

outFile.write(htmlbody)

# SETTING UP TIMESLIDER. ---------------------------------------------------------------------------------------------------------------------------------------------------

# DETERMINING ORTHO IMAGERY IMAGES' UNIQUE YEARS.
years2=[] #Empty array that the ortho imagery years will be appended to.
for x in [1999,2002,2005,2007,2010,2014]: ### ADD TO THIS LIST IF MORE LAYERS ARE AVAILABLE on the tile.mcmaster.ca server.
      years2.append(x) 
orthoYears=sorted(set(years2)) #This is the list of sorted years with ortho imagery.

# DETERMINING FIP IMAGES' UNIQUE YEARS.
years3=[] #Empty array that the FIP years will be appended to.
for x in [1898,1911]: ### ADD TO THIS LIST IF MORE LAYERS ARE AVAILABLE on the tile.mcmaster.ca server.
      years3.append(x) 
FIPYears=sorted(set(years3)) #This is the list of sorted years with FIP images.

# ADDING TIMESLIDER TO BODY. NOTE THAT THE TIMESLIDER INLCUDES ONLY THE YEARS FOR WHICH METADATA IN THE TSV FILE IS AVAILABLE.
uniqueYears=sorted(set(markerYears)|set(orthoYears)|set(FIPYears))
leng=len(uniqueYears) -1
timeslider='<fieldset class="align-center" id="whatever"> \n <input type="text" id="slide" data-slider="true" data-slider-values='+",".join(str(i) for i in markerYears)+' data-slider-snap="true" value=1919> \n '
outFile.write(timeslider)
timesliderclose='<label class="align-left" for=year>'+str(markerYears[0])+'</label><label class="align-right" for=year>'+str(markerYears[-1])+'</label> \n <script> \n $("[data-slider]") \n .each(function () { \n var input = $(this); \n $("<span>") \n .addClass("output") \n .attr("id", "newId") \n .insertAfter($(this)); \n }) \n .bind("slider:ready slider:changed", function (event, data) { \n $(this) \n .nextAll(".output") \n .html(data.value.toFixed(0)); \n }); \n $("<span>").text("Selected Year: ").insertBefore($("#newId")); \n $(document).ready(function()\n{$("body").on("click",":radio",function(evt) {radio(evt.target.layerId);});\n}); \n</script> \n</fieldset>\n</body>\n'
outFile.write(timesliderclose) #Write functions for displaying the value of the timeslider and for obtaining the layer that has been clicked in the layer control window.

# WRITING SCRIPT FOR ALL AERIAL PHOTOS AND CORRESPONDING MARKERS. --------------------------------------------------------------------------------------------------------------

# BEGINNING SCRIPTS.
scripts='<script src="data/exp_AirOrthoAttributeGraph.js"></script> \n <script> \n \n'
outFile.write(scripts) #Write html to draw scripts.

# CREATING MARKERS FROM SPREADSHEET AND WRITING DIFFERENT MARKER COLOURS.
markercolours=['blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen'] #Note that all of these colours correspond to an image of the marker hosted on our MDG wordpress blog.
shadowURL='\'http://en.unesco.org/sites/all/libraries/leaflet/images/marker-shadow.png\''
for colour in markercolours:
    markerURL='\'https://mdgmcmaster.files.wordpress.com/2015/05/'+str(colour)+'.png?w=25\''
    varIcon='var '+str(colour)+'Icon=L.icon({iconUrl: '+str(markerURL)+', shadowUrl: '+str(shadowURL)+', iconAnchor: [12.5,41], popupAnchor: [0,-40]});\n \n'
    outFile.write(varIcon) #Creates an icon associated with each colour from the markercolours array and writes it to the outFile.

markercolours=['blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen', 'blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen', 'blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen', 'blue', 'orange', 'green', 'purple', 'yellow', 'red',  'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen']
flightLine=[] #Creates an empty array where all flight lines of the same year will be stored.
yearlayers=[] #Creates an empty array where all the different year layer groups will be mentioned.
FIPbounds=[] #Creates an empty array where all the different FIP bounds will be mentioned.
yfl=[]
id={}

for x in xrange(0, len(markerYears)): #Iterates through each unique year.
	z=1 #Numbers each different markers for labeling their variable name in the javascript of outFile.
	markerarray=[] #Create empty array for all markers of the same year.
	layerarray=[] #Create empty array for all layers of the same year.
	yflightline=[]
	for line in content:
		item=line.split('\t') #Splitting each line into items at each tab.
		year=item[17] 
		year=year[:4]
		flightline=item[1] #The photo's flightline is in the second column.
		if str(markerYears[x])==year: #If the year is equal to the first value in the cell (year) then append the corresponding flightline to the flightLine array.
			flightLine.append(item[5]) 
		flightLine=sorted(set(flightLine)) #Sort the flightlines for the unique year.
	for line in content:
		item=line.split('\t')
		year=item[17]
		if year[0]=='[':
			year=year[1:-1]
		year=year[:4]
		ID=item[2]
		flightline=item[5]
		photo=item[6]
		scale=item[7]
		latitude=item[8]
		longitude=item[9]
		img=item[10]
		imglink=item[11]
		citationa=item[37]
		citationb=item[38]
		citationc=item[39]
		cflightline=flightline.translate(None,"-")
		cflightline=cflightline.translate(None,"?")
		cflightline=cflightline.translate(None,"/")
		cphoto=photo.translate(None," ")
		cphoto=cphoto.translate(None,"[")
		cphoto=cphoto.translate(None,"]")
		if img=="":
			imgsrc="" #If there is no value in the image column (img="") then don't do anything.
		else:
			imgsrc='<a href="'+str(imglink)+'" target="_blank"><img src="'+str(img)+'" height="200" width="200"></a> <br>' #If image field is not empty then add the image.
		if str(markerYears[x])==year:
			yfl.append(flightline)
	yfl=sorted(set(yfl))
	for line in content:
		item=line.split('\t')
		for z in xrange (0, len(item)-1):
			interest=item[z]
			if interest.startswith('"') and interest.endswith('"'):
				item[z]=interest[1:-1] #Removing the quotations ("") from any item that includes quotations.
		year=item[17]
		if year[0]=='[':
			year=year[1:-1]
		year=year[:4]
		dateother=item[17]
		ID=item[3]
		flightline=item[5]
		photo=item[6]
		scale=item[7]
		latitude=item[8]
		longitude=item[9]
		img=item[10]
		dArchive=item[11]
		citationa=item[37]
		citationb=item[38]
		citationc=item[39]
		cflightline=flightline.translate(None,"-")
		cphoto=photo.translate(None," ")
		cphoto=cphoto.translate(None,"[")
		cphoto=cphoto.translate(None,"]")
		cphoto=cphoto.translate(None,"/")
		cflightline=cflightline.translate(None,"/")
		cflightline=cflightline.translate(None,"\'")
		if flightline=='' and photo=='':
			iTitle=item[0]
			iphoto=item[0]
		else:
			iTitle=''
			iphoto=photo
		iTitle=iTitle.translate(None," ")
		iTitle=iTitle.translate(None,"-")
		iTitle=iTitle.translate(None," ")
		iTitle=iTitle.translate(None,"[")
		iTitle=iTitle.translate(None,"]")
		iTitle=iTitle.translate(None,"/")
		iTitle=iTitle.translate(None,",")
		if dArchive!="":
			dalink='<a href="'+str(dArchive)+'" target="_blank">View/Download the Full-sized Image</a>'
		else:
			dalink=""
		if img=="":
			imgsrc="" #If there is no value in the image column (img="") then don't do anything.
		else:
			imgsrc='<a href="'+str(dArchive)+'" target="_blank"><img src="'+str(img)+'" height="200" width="200"></a> <br>' #If image field is not empty then add the image.

		for y in xrange (0, len(yfl)):
			if flightline==yfl[y] and str(markerYears[x])==year:
				markers='var '+str(ID)+str(markerYears[x])+str(cflightline)+str(cphoto)+str(iTitle)+'=L.marker(['+str(latitude)+','+str(longitude)+'], {icon: '+str(markercolours[y])+'Icon, time: "'+str(dateother)+'"}).bindPopup(\''+str(imgsrc)+'<strong>Set Name</strong> '+str(ID)+' '+str(dateother)+' <br><strong>Photo Date</strong> '+str(item[4])+' <br><strong>Flight Line</strong> '+str(flightline)+'<br> <strong>Photo</strong> '+str(iphoto)+'<br> <strong>Scale</strong> '+str(scale)+'<br> <strong>Citation</strong> '+str(citationa)+'<i>'+str(citationb)+'</i>'+str(citationc)+'<br> '+str(dalink)+'\'); \n'
				outFile.write(markers)
				markerarray.append(str(str(ID)+str(markerYears[x]))+str(cflightline)+str(cphoto)+str(iTitle)) #Writing name of the marker above to the marker array.
			else: pass
			
	if markerYears[x] in markerYears:
		layerarray.append('Markers'+str(markerYears[x]))
		
	markerarray=sorted(set(markerarray)) #Sorting the marker array.
	markerarrayNQ=str(markerarray).translate(None,"'") #Removing quotations from the marker array so that it can be read in javascript (ex. ['a', 'b'] becomes [a, b].
	markerGroup='var Markers'+str(markerYears[x])+'=L.markerClusterGroup({disableClusteringAtZoom:13}).addLayers('+str(markerarrayNQ)+'); \n \n' #Grouping all markers by year in a marker cluster group read by javascript.

	layerarray=sorted(set(layerarray)) #Sorting the layer array.
	layerarrayNQ=str(layerarray).translate(None,"'") #Removing quotations from the marker array so that it can be read in javascript (ex. ['a', 'b'] becomes [a, b].
	layerGroup='var Hamilton'+str(markerYears[x])+'=L.featureGroup('+str(layerarrayNQ)+'); \n \n' #Grouping all layers by year.
	yearlayers.append('Hamilton'+str(markerYears[x])) #Adding each layerGroup created (from each year) to the massive array of all layers (yearlayers).
	id[str(markerYears[x])]='Hamilton'+str(markerYears[x])
	outFile.write(markerGroup)
	outFile.write(layerGroup)
	yfl = []

# WRITING SCRIPT FOR ORTHO IMAGERY AND FIRE INSURANCE PLANS. --------------------------------------------------------------------------------------------------------------

orthoarray=[]
FIParray=[]

for x in xrange(0, len(uniqueYears)): #Iterates through each year.
	if uniqueYears[x] in orthoYears:
		layer = "var Hamilton_"+str(uniqueYears[x])+" = L.tileLayer('http://tiles.mcmaster.ca/Hamilton_"+str(uniqueYears[x])+"/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 19});\n"
		outFile.write(layer) #Writing Ortho Layer variable in java to the outFile.
		orthoarray.append('\"Hamilton '+str(uniqueYears[x])+'\": Hamilton_'+str(uniqueYears[x]))
	else: pass
	if uniqueYears[x] in FIPYears:
		layer = "var FIP_"+str(uniqueYears[x])+" = L.tileLayer('http://perec.mcmaster.ca/maps/FIP_"+str(uniqueYears[x])+"/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 20});\n"
		outFile.write(layer) #Writing FIP layer variable in java to the outFile.
		bound = "var bound_"+str(uniqueYears[x])+" =L.geoJson(B_"+str(uniqueYears[x])+",{style:{'fillOpacity':0,'opacity':0}});\n" 
		outFile.write(bound) # Writing FIP bound variable in java to the outFile.
		FIP = "var FIP"+str(uniqueYears[x])+" =L.featureGroup([FIP_"+str(uniqueYears[x])+", bound_"+str(uniqueYears[x])+"]);\n"
		outFile.write(FIP)
		FIPbounds.append('bound_'+str(uniqueYears[x])) # This set of bounds is to be used for dynamic zooming to the level of the FIPs.
		FIParray.append('\"Hamilton '+str(uniqueYears[x])+'\": FIP'+str(uniqueYears[x]))
	else: pass
	
yearlayers=sorted(set(yearlayers))
FIPbounds=sorted(set(FIPbounds))
orthoarray=sorted(set(orthoarray))
FIParray=sorted(set(FIParray))

# WRITING SCRIPT FOR TOPOGRAPHICAL MAPS. -------------------------------------------------------------------------------------------------------------------------------------------------

TopographyYear = """
var Topography1919 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1919/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1927 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1927/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1934 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1934/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1943 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1943/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1950 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1943/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1951 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1943/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1952 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1952/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1953 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1952/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1954 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1952/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1955 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1952/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1956 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1956/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1958 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1956/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1959 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1956/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1960 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1956/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1961 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1956/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1962 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1956/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1963 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1963/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1964 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1963/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1965 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1963/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1966 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1963/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1967 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1963/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1969 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1969/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1970 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1969/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1972 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1972/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1978 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1978/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1980 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1980/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1985 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1985/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1988 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1985/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1990 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1985/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1994 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1994/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1997 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1997/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography1999 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1999/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
var Topography2000 = L.tileLayer('http://perec.mcmaster.ca/maps/topos/1999/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 16});
"""

TopographyControls = """
var TopographyToggle = L.tileLayer('');
var Topography = L.layerGroup([Topography1919, Topography1927, Topography1934, Topography1943, Topography1950, Topography1951, Topography1952, Topography1953, Topography1954, Topography1955, Topography1956, Topography1958, Topography1959, Topography1960, Topography1961, Topography1962, Topography1963, Topography1964, Topography1965, Topography1966, Topography1967, Topography1969, Topography1970, Topography1972, Topography1978, Topography1980, Topography1985, Topography1988, Topography1990, Topography1994, Topography1997, Topography1999, Topography2000]);

var topoid = {1919: Topography1919, 1927: Topography1927, 1934: Topography1934, 1943: Topography1943, 1950: Topography1950, 1951: Topography1951, 1952: Topography1952, 1953: Topography1953, 1954: Topography1954, 1955: Topography1955, 1956: Topography1956, 1958: Topography1958, 1959: Topography1959, 1960: Topography1960, 1961: Topography1961, 1962: Topography1962, 1963: Topography1963, 1964: Topography1964, 1965: Topography1965, 1966: Topography1966, 1967: Topography1967, 1969: Topography1969, 1970: Topography1970, 1972: Topography1972, 1978: Topography1978, 1980: Topography1980, 1985: Topography1985, 1988: Topography1988, 1990: Topography1990, 1994: Topography1994, 1997: Topography1997, 1999: Topography1999, 2000: Topography2000};
"""

outFile.write(TopographyYear)
outFile.write(TopographyControls)

# WRITING SCRIPT FOR BASEMAPS. -------------------------------------------------------------------------------------------------------------------------------------------------

# ADDING BASEMAPS.
Basemaps="var mbAttr = 'Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, ' +\n'<a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, ' +\n'Imagery © <a href=\"http://mapbox.com\">Mapbox</a>' \nvar osmattr='Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, ' +\n'<a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>'\nvar mbUrl2 = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoibmlja2x1eW1lcyIsImEiOiJjaWhzM2dsem4wMGs2dGZraGY1MzN3YmZ2In0.fDtuZ8EU3C5330xaVS4l6A'\nvar grayscale = L.tileLayer(mbUrl2,{id: 'mapbox.light',maxZoom: 19, attribution: mbAttr}),\nOSMbase = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19,attribution: osmattr}),\nstreets =	L.tileLayer(mbUrl2,{id: 'mapbox.high-contrast',maxZoom: 19, attribution: mbAttr});\n\n"
outFile.write(Basemaps) #Writing java for basemaps to outFile.

# CREATING MAP.
Lmap='var map=L.map(\'map\', {center:[43.26,-79.89],zoom: 11,layers:[OSMbase]}); \n\n' #str() says that the lowest year will be turned on when the map starts up.
outFile.write(Lmap) #Writing map to outFile.
FIPlayers=str(FIPbounds).translate(None,"'") #Removing single quotations from all years in array FIPlayers.
outFile.write('var FIP=L.featureGroup('+str(FIPlayers)+'); \n')
outFile.write("map.on('layeradd', function (e) {if (FIP.hasLayer(e.layer)){(map.fitBounds(e.layer.getBounds()))};})\n\n") #Dynamic zooming to the extent of the FIPs.
yearlayerz=str(yearlayers).translate(None,"'") #Removing single quotations from all years in array yearlayers.
outFile.write('var Years=L.layerGroup('+str(yearlayerz)+'); \n\n')
ids=str(id).translate(None,"'") #ID array to allow for adding layers based on timeslider values.
outFile.write('var id='+str(ids)+'; \n') 
orthoarrayz=str(orthoarray).translate(None,"'").translate(None,"]").translate(None,"[") #Removing single quotations and square brackets from all years in array orthoarray.
FIParrayz=str(FIParray).translate(None,"'").translate(None,"]").translate(None,"[") #Removing single quotations and square brackets from all years in array FIParray.
outFile.write('var baseLayers = {"OSM": OSMbase,"Grayscale": grayscale,"Streets": streets}; \n') 
outFile.write('var overlays = {"Ortho Imagery":{'+str(orthoarrayz)+'},\n"Fire Insurance Plans":{'+str(FIParrayz)+'},"Topographical Maps":{"Hamilton": TopographyToggle'+'}};\n\n') #Baselayers and overlays to be used for the basemap layer control.

# BASEMAP LAYER CONTROL.
LCGBasemaps='var control = L.control.groupedLayers(baseLayers, overlays,{exclusiveGroups: ["Ortho Imagery","Fire Insurance Plans","Topographical Maps"],collapsed:false}).addTo(map); \n\n' #Adding layer control to the 'map' variable.
outFile.write(LCGBasemaps)

# WRITING SCRIPT FOR MAP FEATURES. -------------------------------------------------------------------------------------------------------------------------------------------------

# ADD SCALE TO MAP.
mapScale='L.control.scale({options: {position: \'bottomleft\',maxWidth: 100,metric: true,imperial: false,updateWhenIdle: false}}).addTo(map); \n\n' #Adding a scale bar to the 'map' variable.
outFile.write(mapScale)

# ADD OPACITY SLIDER.
opacFunction='slider = L.control.slider(function(value) {'
outFile.write(opacFunction)
for x in xrange(0,len(orthoYears)):
	opacLayer='Hamilton_'+str(orthoYears[x])+'.setOpacity(value);'
	outFile.write(opacLayer)
for x in xrange(0,len(FIPYears)):
	opacLayer='FIP_'+str(FIPYears[x])+'.setOpacity(value);'
	outFile.write(opacLayer)
opacEnd='Topography1919.setOpacity(value);Topography1927.setOpacity(value);Topography1934.setOpacity(value);Topography1943.setOpacity(value);Topography1950.setOpacity(value);Topography1951.setOpacity(value);Topography1952.setOpacity(value);Topography1953.setOpacity(value);Topography1954.setOpacity(value);Topography1955.setOpacity(value);Topography1956.setOpacity(value);Topography1958.setOpacity(value);Topography1959.setOpacity(value);Topography1960.setOpacity(value);Topography1961.setOpacity(value);Topography1962.setOpacity(value);Topography1963.setOpacity(value);Topography1964.setOpacity(value);Topography1965.setOpacity(value);Topography1966.setOpacity(value);Topography1967.setOpacity(value);Topography1969.setOpacity(value);Topography1970.setOpacity(value);Topography1972.setOpacity(value);Topography1978.setOpacity(value);Topography1980.setOpacity(value);Topography1985.setOpacity(value);Topography1988.setOpacity(value);Topography1990.setOpacity(value);Topography1994.setOpacity(value);Topography1997.setOpacity(value);Topography1999.setOpacity(value);Topography2000.setOpacity(value);},\n{position: "topright",max: 1,value: 1,step:0.05,size: "200px",collapsed: false,id: "slider"}).addTo(map);\n\n'
outFile.write(opacEnd) #Add opacity slider to the map for the orthophotos and FIPs.

# BASEMAP LAYER CONTROL CHANGE TIMESLIDER VALUE.
sliderval='function radio(layerid)\n{obj = control._layers[layerid];\nfor(var key in id) {\n  if(id[key] === obj.layer) {$("#slide").simpleSlider("setValue", key);};\n};}\n\n'
outFile.write(sliderval) #Change the timeslider value based on overlay clicked in layer control.

# TIMESLIDER SWITCHING BETWEEN YEARS.
yearswitch="""
function layer(value)
  {if (map.hasLayer(id[value])==false) {map.eachLayer(function(layer){
		if (Years.hasLayer(layer)==true) {map.removeLayer(layer)}});
		id[value].addTo(map).bringToFront();};
	if (map.hasLayer(TopographyToggle)==true) {
		if (map.hasLayer(topoid[value])==false) {map.eachLayer(function(layer){
			if (Topography.hasLayer(layer)==true) {map.removeLayer(layer)}});
			topoid[value].addTo(map).bringToFront();};}
	if (map.hasLayer(TopographyToggle)==false) {
		if (map.hasLayer(topoid[value])==true) {map.eachLayer(function(layer){
			if (Topography.hasLayer(layer)==true) {map.removeLayer(layer)}})
			}}
	};
"""

outFile.write(yearswitch) #Based on timeslider value, add layers to the map.

# TIMESLIDER FUNCTION.
timesliderfunc = '$("body").mousemove(function() { \n layer(Number($("#newId").text())); \n });\n\n' 
outFile.write(timesliderfunc) #Get value from timeslider to use in the previous function.

# CLOSE SCRIPT.
closescript='</script> \n\n'
outFile.write(closescript) #Closes script.

# CLOSE HTML.
Closehtml='\n \n </html>'
outFile.write(Closehtml) #Closes html.

# WRITING COMPLETION ALERT.
print ("The map's webpage code has been written to the html file named " + str(outfn) + ".")
inFile.close()
outFile.close()
