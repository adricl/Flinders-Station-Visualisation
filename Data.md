# Flinders St Station Data

### Data Midi
https://github.com/cirlabs/miditime
https://programminghistorian.org/en/lessons/sonification

More hints on what to do https://www.youtube.com/watch?v=vFItEfPHp2A
he uses the c note pentatonic sclae for the random notes
Use a few differnet tracks. 

Random velocity makes it sounds more human
Increase the note length for an intrument. 
CHange chords randomly 

## Air Quality Hourly Data
https://discover.data.vic.gov.au/dataset/1a673fd7-e5fe-4aed-ae8d-3537d088f1bd/resource/645643b0-e6a6-49de-bce2-895e37b0b1c2/download/epa20-20aqapi20-20web20services20specification20v12032028229.pdf
http://sciwebsvc.epa.vic.gov.au/aqapi/Help

Siteid = 10239 Melbourne CBD
AQI - Air Quality Index is a number used by government agencies to communicate to
the public how polluted the air currently is.
AQI:
http://sciwebsvc.epa.vic.gov.au/aqapi/Measurements?siteId=10239&monitorId=sp_AQI&timebasisid=1HR_AV&fromDate=20190627&toDate=20190628

BPM2.5 - Particles as PM2.5
http://sciwebsvc.epa.vic.gov.au/aqapi/StationData?pointid=10239 data for 24 hours of 1 hour interval data.
http://www.epa.vic.gov.au/your-environment/air/air-pollution/pm25-particles-in-air
http://sciwebsvc.epa.vic.gov.au/aqapi/Measurements?siteId=10239&monitorId=BPM2.5&timebasisid=1HR_AV&fromDate=20190627&toDate=20190628

### Foot Trafic Data
https://dev.socrata.com/foundry/data.melbourne.vic.gov.au/d6mv-s43h
        "sensor_id": "41",
        "sensor_description": "Flinders La-Swanston St (West)",
        "sensor_name": "Swa31",
        
        "sensor_id": "22",
        "sensor_description": "Flinders St-Elizabeth St (East)",
        "sensor_name": "Eli274_T",
        
        "sensor_id": "5",
        "sensor_description": "Princes Bridge",
        "sensor_name": "PriNW_T",
        
        "sensor_id": "6",
        "sensor_description": "Flinders Street Station Underpass",
        "sensor_name": "FliS_T",
        "installation_date": "2009-03-25T00:00:00.000",
        
        Data
        https://data.melbourne.vic.gov.au/resource/d6mv-s43h.json?$where=sensor_id in (41, 22, 5, 6) 
        
### Bike Date Flinders every 15 mins
https://data.melbourne.vic.gov.au/resource/tdvh-n9dv.json?station_id=10
List of dock locations https://data.melbourne.vic.gov.au/Transport-Movement/Bike-Share-Dock-Locations/vrwc-rwgm/data

### Parking Car data every few mins
https://data.melbourne.vic.gov.au/Transport-Movement/On-street-Parking-Bay-Sensors/vh2v-4nfs?_ga=2.99972502.941783241.1562311319-1939482522.1561725981

### Car Bluetooth Data
https://vicroadsopendata-vicroadsmaps.opendata.arcgis.com/datasets/bluetooth-travel-time-updates-every-2-minutes
Object ids:42737, 29240, 21971, 3762, 36401, 222, 40769 , 53260, 14668, 45891, 33294, 36318, 32647, 6607, 15101, 6659, 28175, 
40846, 53855, 38769, 12352, 58209, 246, 50480, 41939, 42737, 29240, 5432, 6802

https://vicdata.vicroads.vic.gov.au/server/rest/services/Operations_Traffic/FeatureServer/1/query?where=1%3D1&outFields=*&geometry=144.954%2C-37.82%2C144.974%2C-37.817&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnGeometry=false&outSR=4326&f=json


https://vicroadsopendata-vicroadsmaps.opendata.arcgis.com/datasets/traffic-volume
https://vicdata.vicroads.vic.gov.au/server/rest/services/Operations_Traffic/FeatureServer/0/query?where=1%3D1&outFields=*&geometry=144.951%2C-37.821%2C144.978%2C-37.815&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnGeometry=false&outSR=4326&f=json

### PTV

Crap Dont Use
GTFS Release - https://github.com/google/transitfeed user this as it works in python 3 https://github.com/google/transitfeed/pull/484

Good https://github.com/remix/partridge

Feed - http://data.ptv.vic.gov.au/downloads/gtfs.zip
https://discover.data.vic.gov.au/dataset/ptv-timetable-and-geographic-information-2015-gtfs
The PTV GTFS data has been exported by operational branches listed in the
folder numbers below:
1 - Regional Train
2 - Metropolitan Train
3 - Metropolitan Tram
4 - Metropolitan Bus 
5 - Regional Coach
6 - Regional Bus
7 - TeleBus
8 – Night Bus
10 - Interstate
11 - SkyBus

