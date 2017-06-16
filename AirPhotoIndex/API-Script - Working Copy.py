# -*- coding: cp1252 -*-
#
# THIS PYTHON SCRIPT CONVERTS INFORMATION FROM THE MASTER SPREADSHEET OF AERIAL PHOTO INDEX METADATA
# IN .TSV FORMAT INTO HTML FORMAT. IN ADDITION TO BASE LAYER MAPS AND MARKERS FOR EACH AERIAL PHOTO
# IN THE DATABASE, THE HTML FILE CREATED WITH THIS SCRIPT INCLUDES LAYERS OF HISTORIC FIRE INSURANCE
# PLANS, ORTHOIMAGERY, AND TOPOGRAPHICAL MAPS. A TUTORIAL MODAL IS ALSO INCLUDED IN THE HTML FILE
# THAT POPS UP UPON OPENING THE WEBPAGE.
#
# MAJORITY OF THE WEBSITE'S FUNCTIONALITY IS USED WITH LEAFLET, AN OPEN-SOURCE JAVASCRIPT LIBRARY FOR
# MOBILE-FRIENDLY INTERACTIVE MAPS. ALL JAVASCRIPT AND CSS FILES USED FOR THIS SCRIPT ARE STORED WITHIN
# THE 'AIRPHOTOINDEX' FOLDER.
#
# Note: The above encoding, cp1252, allows the recognition of non ASCII characters within this script.

import os
import sys
import codecs

# SETTING INPUT AND OUTPUT FILES.

#----------------------------------------------------------------------------- USER EDIT ---------
# Opening the metadata file located in the directory of this script.
# DEAR USER: Enter the corresponding filename for a tsv file containing the aerial photo metadata.
inFile = open('Master.tsv')

#----------------------------------------------------------------------------- USER EDIT ---------
# Defining the HTML file located in the directory of this script.
# DEAR USER: Enter the filename for the desired HTML file. this script will be written to.
outfn = 'index.html'

# Checking if output filename exists and removing it if it does.
if os.path.exists(outfn):
	
	print 'It appears that ' + outfn + ' already exists! Please wait while it is removed and replaced...' 
	os.remove(outfn)
	
else:
	print outfn +' does not already exist! Please wait while it is created...'

# Opening the output file this script will write to.
outFile = open(outfn, 'w') 

# READING TSV FILE AND OBTAINING DATA.

allcontent = inFile.readlines()
content = allcontent[3:] # This list excludes the titles from the tsv file.

# Obtaining unique years from corresponding column in the metadata.
years = [] # Creating list of all years.

for line in content:
	
	item = line.split('\t')
	year = item[17]
	
	if year[0] == '[':
		year = year[1:-1]

	#In the case where item[17] is a range of years, the earliest year is considered.    
	year = year[:4]
	years.append(year)

# Obtaining the set of unique years used for the timeslider, and sorting them in ascending order.
timelineyears = sorted(set(years)) 
timelineyears = map(int,timelineyears)

# WRITING THE BEGINNING OF THE HTML CODE TO index.html.

# Writing the website's head elements, which are stored in a text file.
openhtml = '<html> \n'
outFile.write(openhtml)
indexhead = open("index_head.txt").readlines()
for line in indexhead:
	outFile.write(line)

# Writing part of the website's body, including the header and pop-up modal.
indexbodybeginning = open("index_body_header_modal.txt").readlines()
for line in indexbodybeginning:
	outFile.write(line)

# SETTING UP TIMESLIDER, AERIAL PHOTOS, AND AERIAL PHOTO MARKERS.

# Defining the unique years for which orthoimagery is available.
orthoyears = [1999,2002,2005,2007,2010,2014]
orthoyears = sorted(set(orthoyears))

# Defining the unique years for which fire insurance plans are available.
fipyears = [1898,1911]
fipyears = sorted(set(fipyears))

uniqueyears = sorted(set(timelineyears)|set(orthoyears)|set(fipyears))
timeslider = '<fieldset class="align-center" id="whatever"> \n <input type="text" id="slide" data-slider="true" data-slider-values='+",".join(str(i) for i in timelineyears)+' data-slider-snap="true" value=1919> \n '
timesliderclose = '<label class="align-left" for=year>'+str(timelineyears[0])+'</label><label class="align-right" for=year>'+str(timelineyears[-1])+'</label> \n <script> \n $("[data-slider]") \n .each(function () { \n var input = $(this); \n $("<span>") \n .addClass("output") \n .attr("id", "newId") \n .insertAfter($(this)); \n }) \n .bind("slider:ready slider:changed", function (event, data) { \n $(this) \n .nextAll(".output") \n .html(data.value.toFixed(0)); \n }); \n $("<span>").text("Selected Year: ").insertBefore($("#newId")); \n $(document).ready(function()\n{$("body").on("click",":radio",function(evt) {radio(evt.target.layerId);});\n}); \n</script> \n</fieldset>\n</body>\n'
scripts = '<script src="data/exp_AirOrthoAttributeGraph.js"></script> \n <script> \n \n'

# Writing functions to display the timeslider year and corresponding layer of "time".
outFile.write(timeslider)
outFile.write(timesliderclose)
outFile.write(scripts)

# Defining marker colours for each image of the marker hosted on the MDG wordpress blog.
markercolours = ['blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen']
shadowURL = '\'http://en.unesco.org/sites/all/libraries/leaflet/images/marker-shadow.png\''

# Creating an icon for each colour from the markercolours array.
for colour in markercolours:
	markerURL = '\'https://mdgmcmaster.files.wordpress.com/2015/05/'+str(colour)+'.png?w=25\''
	varIcon = 'var '+str(colour)+'Icon=L.icon({iconUrl: '+str(markerURL)+', shadowUrl: '+str(shadowURL)+', iconAnchor: [12.5,41], popupAnchor: [0,-40]});\n \n'
	outFile.write(varIcon) 

# Redefining marker colours to repeat after having each been used once.
markercolours = ['blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen', 'blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen', 'blue', 'orange', 'green', 'purple', 'yellow', 'red', 'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen', 'blue', 'orange', 'green', 'purple', 'yellow', 'red',  'pink', 'gray', 'maroon', 'brown', 'lightblue', 'lightgreen']

# Creating empty lists.
flightlineset = [] # Creating a set for all flightlines of the same timeline year.
yearlayers = [] # Creating list of the different year layer groups mentioned.
FIPbounds = [] # Creating list of all the different FIP bounds mentioned.
id = {}

# Obtaining corresponding metadata for each timeline year.
for x in xrange(0, len(timelineyears)):

	z = 1

	# Creating empty lists.
	markerarray = [] # Creating list for all markers of the same flightline and timeline year.
	layerarray = [] # Create list for all layers of the same timeline year.
	yflightline = []

	# Obtaining a set of all flightlines of the same timeline year. This set is created in a
	# seperate loop than the following, as the following uses the previously defined variable,
	# 'flightlineset'.
	for line in content:

		item = line.split('\t')
		
		# Obtaining the timeline year for each aerial photo.
		year = item[17]
		if year[0] == '[':
			year = year[1:-1]
		year = year[:4]

		if str(timelineyears[x]) == year:
			flightlineset.append(item[5])
			
	flightlineset=sorted(set(flightlineset))

	# Obtaining the metadata for each aerial photo's pop-up.
	for line in content:

		item=line.split('\t')

		# Removing quotations from any items in the TSV file to be read by javascript.
		for z in xrange (0, len(item)-1):
			interest = item[z]
			if interest.startswith('"') and interest.endswith('"'):
				item[z] = interest[1:-1]
				
		# Obtaining the timeline year for each aerial photo.
		year = item[17]
		if year[0] == '[':
			year = year[1:-1]
		year = year[:4]

		# For each aerial photo, the set name, photo date, flight line, photo number, scale,
		# citation, thumbnail, thumbnail link, and digital archvie link is obtained from their
		# respective columns in the TSV file.	
		identifier = item[3]
		flightline = item[5]
		photo = item[6]
		scale = item[7]
		latitude = item[8]
		longitude = item[9]
		thumbnail = item[10]
		archivelink = item[11]
		fulldate = item[17]
		citationa = item[37]
		citationb = item[38]
		citationc = item[39]

		# If there is no information for both the flightline or photo, this sets the title for
		# both information fields.
		if flightline == '' and photo == '':
        
			iTitle = item[0]
			iphoto = item[0]
			
		else:
			iTitle = ''
			iphoto = photo

                # Formatting information.
		cflightline = flightline.translate(None,"-")
		cflightline = cflightline.translate(None,"?")
		cflightline = cflightline.translate(None,"/")
		cflightline = cflightline.translate(None,"\'")
		cphoto = photo.translate(None," ")
		cphoto = cphoto.translate(None,"[")
		cphoto = cphoto.translate(None,"]")
		cphoto = cphoto.translate(None,"/")
		iTitle = iTitle.translate(None," ")
		iTitle = iTitle.translate(None,"-")
		iTitle = iTitle.translate(None," ")
		iTitle = iTitle.translate(None,"[")
		iTitle = iTitle.translate(None,"]")
		iTitle = iTitle.translate(None,"/")
		iTitle = iTitle.translate(None,",")

		# If a link to the Digital Archive exists, this writes the neccessary HTML code.
		if archivelink != "":
			archivelinkscript = '<a href="'+str(archivelink)+'" target="_blank">View/Download the Full-sized Image</a>'
		else:
			archivelinkscript = ""

		# If the thumbnail image exists, this writes the necessary HTML code.	
		if thumbnail == "":
			thumbnailscript = ""
		else:
			thumbnailscript='<a href="'+str(archivelink)+'" target="_blank"><img src="'+str(thumbnail)+'" height="200" width="200"></a> <br>'

                # !IMPORTANT! # Creates script for a marker function for each aerial photo marker.
                # !IMPORTANT! # The information for each aerial photo pop-up is created here.
                # !IMPORTANT! # To make all aerial photos of the same flightline the same colour,
                # !IMPORTANT! # the list markerarray is created to store aerial photos for the same
                # !IMPORTANT! # flightline and timeline year.
		for y in xrange (0, len(flightlineset)):
                        
			if flightline == flightlineset[y] and str(timelineyears[x])==year:

                                # Creating each marker.
				markers = 'var '+str(identifier)+str(timelineyears[x])+str(cflightline)+str(cphoto)+str(iTitle)+'=L.marker(['+str(latitude)+','+str(longitude)+'], {icon: '+str(markercolours[y])+'Icon, time: "'+str(fulldate)+'"}).bindPopup(\''+str(thumbnailscript)+'<br><strong>Set Name</strong> '+str(identifier)+' '+str(fulldate)+' <br><strong>Photo Date</strong> '+str(item[4])+' <br><strong>Flight Line</strong> '+str(flightline)+'<br> <strong>Photo</strong> '+str(iphoto)+'<br> <strong>Scale</strong> '+str(scale)+'<br> <strong>Citation</strong> '+str(citationa)+'<i>'+str(citationb)+'</i>'+str(citationc)+'<br> '+str(archivelinkscript)+'\'); \n'
				outFile.write(markers)

				# Appending the name of individual markers to a set of all markers for the same flightline.
				markerarray.append(str(str(identifier)+str(timelineyears[x]))+str(cflightline)+str(cphoto)+str(iTitle))
				
			else: pass

	# Appending all marker sets to a list of marker sets of the same timeline year.		
	if timelineyears[x] in timelineyears:
		layerarray.append('Markers'+str(timelineyears[x]))

	# Sorting and removing quotation from arrays to be read in javascript.
	markerarray = sorted(set(markerarray))
	layerarray = sorted(set(layerarray))
	markerarrayNQ = str(markerarray).translate(None,"'")
	layerarrayNQ = str(layerarray).translate(None,"'")

	# 
	markerGroup = 'var Markers'+str(timelineyears[x])+'=L.markerClusterGroup({disableClusteringAtZoom:13}).addLayers('+str(markerarrayNQ)+'); \n \n' # Grouping all markers by year in a marker cluster group read by javascript.
	layerGroup = 'var Hamilton'+str(timelineyears[x])+'=L.featureGroup('+str(layerarrayNQ)+'); \n \n' # Grouping all layers by year.
	yearlayers.append('Hamilton'+str(timelineyears[x])) # Adding each layerGroup created (from each year) to the massive array of all layers (yearlayers).
	id[str(timelineyears[x])] = 'Hamilton'+str(timelineyears[x])
	outFile.write(markerGroup)
	outFile.write(layerGroup)
	flightlineset = []

# WRITING SCRIPT FOR ORTHO IMAGERY AND FIRE INSURANCE PLANS.

orthoarray=[]
FIParray=[]

for x in xrange(0, len(uniqueyears)): # Iterates through each year.
	if uniqueyears[x] in orthoyears:
		layer = "var Hamilton_"+str(uniqueyears[x])+" = L.tileLayer('http://tiles.mcmaster.ca/Hamilton_"+str(uniqueyears[x])+"/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 19});\n"
		outFile.write(layer) # Writing Ortho Layer variable in java to the outFile.
		orthoarray.append('\"Hamilton '+str(uniqueyears[x])+'\": Hamilton_'+str(uniqueyears[x]))
	else: pass
	if uniqueyears[x] in fipyears:
		layer = "var FIP_"+str(uniqueyears[x])+" = L.tileLayer('http://perec.mcmaster.ca/maps/FIP_"+str(uniqueyears[x])+"/{z}/{x}/{y}.png', {format: 'image/png',tms: true,noWrap: true,maxZoom: 20});\n"
		outFile.write(layer) # Writing FIP layer variable in java to the outFile.
		bound = "var bound_"+str(uniqueyears[x])+" =L.geoJson(B_"+str(uniqueyears[x])+",{style:{'fillOpacity':0,'opacity':0}});\n" 
		outFile.write(bound) # Writing FIP bound variable in java to the outFile.
		FIP = "var FIP"+str(uniqueyears[x])+" =L.featureGroup([FIP_"+str(uniqueyears[x])+", bound_"+str(uniqueyears[x])+"]);\n"
		outFile.write(FIP)
		FIPbounds.append('bound_'+str(uniqueyears[x])) # This set of bounds is to be used for dynamic zooming to the level of the FIPs.
		FIParray.append('\"Hamilton '+str(uniqueyears[x])+'\": FIP'+str(uniqueyears[x]))
	else: pass
	
yearlayers=sorted(set(yearlayers))
FIPbounds=sorted(set(FIPbounds))
orthoarray=sorted(set(orthoarray))
FIParray=sorted(set(FIParray))

# WRITING SCRIPT FOR TOPOGRAPHICAL MAPS.

# This section of the script first creates variables for the corresponding set of latest topographical
# maps for each year on the time slider. Then controllable variables are created and used in
# function(layer) near the end of the html code. TopographyToggle is a blank layer controlled by
# the user-clickable bubble for the Hamilton's topography. Lastly, citations were created for each
# section of topography and attached to an invisible polygon around each corresponding quarter section
# of the Hamilton topography layer.

indexbodytopography = open("index_body_topography.txt").readlines()
for line in indexbodytopography:
	outFile.write(line)

# WRITING SCRIPT FOR BASEMAPS, MAP, AND MAP FEATURES.

# Writing javascript for basemaps OpenStreetMap, Streets, and Grayscale.
Basemaps="var mbAttr = 'Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, ' +\n'<a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, ' +\n'Imagery © <a href=\"http://mapbox.com\">Mapbox</a>' \nvar osmattr='Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, ' +\n'<a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>'\nvar mbUrl2 = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoibmlja2x1eW1lcyIsImEiOiJjaWhzM2dsem4wMGs2dGZraGY1MzN3YmZ2In0.fDtuZ8EU3C5330xaVS4l6A'\nvar grayscale = L.tileLayer(mbUrl2,{id: 'mapbox.light',maxZoom: 19, attribution: mbAttr}),\nOSMbase = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19,attribution: osmattr}),\nstreets =    L.tileLayer(mbUrl2,{id: 'mapbox.high-contrast',maxZoom: 19, attribution: mbAttr});\n\n"
outFile.write(Basemaps)

# Creating map.
Lmap='var map=L.map(\'map\', {center:[43.26,-79.89],zoom: 11,layers:[OSMbase]}); \n\n'
outFile.write(Lmap)

# Adding dynamic zooming to the extent of the FIPs.
FIPlayers=str(FIPbounds).translate(None,"'") # Removing single quotations.
outFile.write('var FIP=L.featureGroup('+str(FIPlayers)+'); \n')
outFile.write("map.on('layeradd', function (e) {if (FIP.hasLayer(e.layer)){(map.fitBounds(e.layer.getBounds()))};})\n\n")

yearlayerz=str(yearlayers).translate(None,"'")
outFile.write('var Years=L.layerGroup('+str(yearlayerz)+'); \n\n')
ids=str(id).translate(None,"'") # identifier array to allow for adding layers based on timeslider values.
outFile.write('var id='+str(ids)+'; \n') 
orthoarrayz=str(orthoarray).translate(None,"'").translate(None,"]").translate(None,"[")
FIParrayz=str(FIParray).translate(None,"'").translate(None,"]").translate(None,"[")

# Wtiting basemaps, overlays, and adding them to layer control.
outFile.write('var baseLayers = {"OpenStreetMap": OSMbase,"Grayscale": grayscale,"Streets": streets}; \n') 
outFile.write('var overlays = {"<b>Orthoimagery</b>":{'+str(orthoarrayz)+'},\n"<b>Fire Insurance Plans</b>":{'+str(FIParrayz)+'},"<b>Topographic Maps</b>":{"Hamilton": TopographyToggle'+'}};\n\n')
LCGBasemaps='var control = L.control.groupedLayers(baseLayers, overlays,{exclusiveGroups: ["Orthoimagery","Fire Insurance Plans","Topographic Maps"],collapsed:false}).addTo(map); \n\n'
outFile.write(LCGBasemaps)

# Adding scale and opacity slider to map.
mapScale='L.control.scale({options: {position: \'bottomleft\',maxWidth: 100,metric: true,imperial: false,updateWhenIdle: false}}).addTo(map); \n\n'
opacFunction='slider = L.control.slider(function(value) {'
outFile.write(mapScale)
outFile.write(opacFunction)

for x in xrange(0,len(orthoyears)):
	opacLayer='Hamilton_'+str(orthoyears[x])+'.setOpacity(value);'
	outFile.write(opacLayer)

for x in xrange(0,len(fipyears)):
	opacLayer='FIP_'+str(fipyears[x])+'.setOpacity(value);'
	outFile.write(opacLayer)

opacEnd='Topography1919.setOpacity(value);Topography1927.setOpacity(value);Topography1934.setOpacity(value);Topography1943.setOpacity(value);Topography1950.setOpacity(value);Topography1951.setOpacity(value);Topography1952.setOpacity(value);Topography1953.setOpacity(value);Topography1954.setOpacity(value);Topography1955.setOpacity(value);Topography1956.setOpacity(value);Topography1958.setOpacity(value);Topography1959.setOpacity(value);Topography1960.setOpacity(value);Topography1961.setOpacity(value);Topography1962.setOpacity(value);Topography1963.setOpacity(value);Topography1964.setOpacity(value);Topography1965.setOpacity(value);Topography1966.setOpacity(value);Topography1967.setOpacity(value);Topography1969.setOpacity(value);Topography1970.setOpacity(value);Topography1972.setOpacity(value);Topography1978.setOpacity(value);Topography1980.setOpacity(value);Topography1985.setOpacity(value);Topography1988.setOpacity(value);Topography1990.setOpacity(value);Topography1994.setOpacity(value);Topography1997.setOpacity(value);Topography1999.setOpacity(value);Topography2000.setOpacity(value);},\n{position: "topright",max: 1,value: 1,step:0.05,size: "200px",collapsed: false,id: "slider"}).addTo(map);\n\n'
outFile.write(opacEnd)

# Writing function to add layers to the map for the corresponding time slider year.
yearswitch = """
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
	if (map.hasLayer(TopographyToggle)==true) {
		if (map.hasLayer(polyid[value])==false) {map.eachLayer(function(layer){
			if (Polygons.hasLayer(layer)==true) {map.removeLayer(layer)}});
			polyid[value].addTo(map).bringToFront();};}
	if (map.hasLayer(TopographyToggle)==false) {
		if (map.hasLayer(polyid[value])==true) {map.eachLayer(function(layer){
			if (Polygons.hasLayer(layer)==true) {map.removeLayer(layer)}});
			}}
	};
"""
outFile.write(yearswitch) 

# Getting value from timeslider to use in the previous function.
timesliderfunc = '$("body").mousemove(function() { \n layer(Number($("#newId").text())); \n });\n\n' 
outFile.write(timesliderfunc) 

# Closing HTML file.
closescript='</script> \n\n'
closehtml='\n \n </html>'
outFile.write(closescript)
outFile.write(closehtml)

print ("Success. The Historical Hamilton Portal HTML file has been written to " + str(outfn) + ".")

inFile.close()
outFile.close()
