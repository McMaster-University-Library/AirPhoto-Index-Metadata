##Notes on changes:

- Best to run a diff on everything in the top 87 lines. I had to convert all http to https, which meant finding new libraries in a variety of places.
- I've updated the leaflet library to 0.7.7 using [this site](https://cdnjs.com/libraries/leaflet/) as a guide; however, if I upgrade to any newer verion, I get an error message:

```
Uncaught TypeError: Cannot read property 'trim' of undefined
    at Object.trim (leaflet.js:5)
    at Object.splitWords (leaflet.js:5)
    at e.on (leaflet.js:5)
    at e.initialize (leaflet.markercluster.js:6)
    at new e (leaflet.js:5)
    at Object.L.markerClusterGroup (leaflet.markercluster.js:6)
    at index.html:262
```

This needs to be investigated.

- change all 
http://library.mcmaster.ca/maps/airphotos/thumbnails/image_not_available.png
to 
https://library.mcmaster.ca/maps/airphotos/thumbnails/image_not_available.png

- change all 
http://digitalarchive.mcmaster.ca////
to 
https://digitalarchive.mcmaster.ca////

http://en.unesco.org
to 
https://en.unesco.org

http://library.mcmaster.ca/maps/airphotos
to 
https://library.mcmaster.ca/maps/airphotos

http://library.mcmaster.ca/maps/collection/fire
to 
https://library.mcmaster.ca/collections/fire-insurance-plans

http://openstreetmap.org
to 
https://openstreetmap.org

http://creativecommons.org/licenses/by-sa/2.0/
to 
https://creativecommons.org/licenses/by-sa/2.0/

http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
to 
https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png

http://mapbox.com
to 
https://mapbox.com

**Essentially**, the only URLs that *shouldn't* be changed to https are:
- http://perec.mcmaster.ca/...
- http://tiles.mcmaster.ca/...

