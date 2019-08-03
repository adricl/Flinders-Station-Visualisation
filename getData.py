import partridge as ptg
import datetime
import os
import pandas as pd
import urllib.request as req
import zipfile
import json

def getTransportData():
  dataName = 'data'
  fileName = 'gtfs.zip'
  if not os.path.exists(dataName):
    os.mkdir(dataName)
  url = 'http://data.ptv.vic.gov.au/downloads/' + fileName
  req.urlretrieve(url, dataName)
  with zipfile.ZipFile(dataName + '/' + fileName, 'r') as zip_ref:
    zip_ref.extractall()


def convertTimeToStr(time):
  split = time.split(':')
  val = int(split[0]) * 60 + int(split[1])
  return val

def loadData(dataType, inpath, dateSelected, stopIds):
  feed = ptg.load_raw_feed(inpath)
  trips = feed.trips
  stops = feed.stops
  stop_times = feed.stop_times
  #stop_ids = stops[stops.stop_id.isin(stopIds)]['stop_id']

  service_id_by_selected_day = {}
  service_ids_by_date = ptg.read_service_ids_by_date(inpath)
  for date, service_id in service_ids_by_date.items():
    if (date == dateSelected.date()):
      service_id_by_selected_day = service_id

  #we create a temp column to sort by
  sort_column = []
  for time in stop_times['arrival_time']:
    sort_column.append(convertTimeToStr(time))
  stop_times['sort_column'] = sort_column

  #default val of type
  stop_times['type'] = dataType

  trip_ids = trips[trips.service_id.isin(service_id_by_selected_day)].trip_id
  filter_by_trips = stop_times[stop_times.trip_id.isin(trip_ids)]
  filter_by_stops = filter_by_trips[filter_by_trips.stop_id.isin(stopIds)]

  #delete unrequired columns
  stop_times = stop_times.drop('stop_headsign', axis=1)
  stop_times = stop_times.drop('pickup_type', axis=1)
  stop_times = stop_times.drop('drop_off_type', axis=1)
  stop_times = stop_times.drop('shape_dist_traveled', axis=1)
  stop_times = stop_times.drop('trip_id', axis=1)

  filter_by_stops_sorted = filter_by_stops.sort_values(by='sort_column', axis=0, ascending=True)
  filter_by_stops_sorted.to_csv(dataType + '.csv')
  return filter_by_stops_sorted

def generateResultData(result):
  transformedData = pd.DataFrame(columns = ['time', 'type', 'arrival_departure', 'sort_column'])

  for index, row in result.iterrows():
    strCmp = convertTimeToStr(row.arrival_time) == convertTimeToStr(row.departure_time)
    if(strCmp and int(row.stop_sequence == 1)):
      transformedData = transformedData.append({'time': row.arrival_time, 'type': row.type, 'arrival_departure': 'departure', 'sort_column': row.sort_column }, ignore_index=True)
    elif(strCmp):
      transformedData = transformedData.append({'time': row.arrival_time, 'type': row.type, 'arrival_departure': 'arrival', 'sort_column': row.sort_column }, ignore_index=True)
    else:
      transformedData = transformedData.append({'time': row.arrival_time, 'type': row.type, 'arrival_departure': 'arrival', 'sort_column': convertTimeToStr(row.arrival_time) }, ignore_index=True)
      transformedData = transformedData.append({'time': row.departure_time, 'type': row.type, 'arrival_departure': 'departure', 'sort_column': convertTimeToStr(row.departure_time) }, ignore_index=True)
  return transformedData.sort_values(by='sort_column', axis=0, ascending=True)
#getTransportData()

#train
inpath = 'data/gtfs/2/google_transit.zip'
dateSelected = datetime.datetime(2019,7,20)
#19854, Flinders Street Railway Station
stopIds = ['19854']
train = loadData('train', inpath, dateSelected, stopIds)

#Regional Train
inpath = 'data/gtfs/1/google_transit.zip'
dateSelected = datetime.datetime(2019,7,20)
#22238, Flinders Street Railway Station
stopIds = ['22238']
regTrain = loadData('regional train', inpath, dateSelected, stopIds)

#Tram
inpath = 'data/gtfs/3/google_transit.zip'
dateSelected = datetime.datetime(2019,7,20)
#19685, 13-Federation Square/Swanston St 
#19499, 13-Federation Square/Swanston St
#18175, 5-Swanston St/Flinders St (Melbourne City)
#18090, 5-Swanston St/Flinders St (Melbourne City)
#18176, 4-Elizabeth St/Flinders St
#18089, 4-Elizabeth St/Flinders St
#17850, 1-Flinders Street Railway Station/Elizabeth St
#17877, 1-Flinders Street Railway Station/Elizabeth St
stopIds = ['19499', '19685', '18090', '18175', '18176', '18089', '17850', '17877']
tram = loadData('tram', inpath, dateSelected, stopIds)

#Night Bus
inpath = 'data/gtfs/8/google_transit.zip'
dateSelected = datetime.datetime(2019,7,20)
stopIds = ['41082']
nightBus = loadData('night bus', inpath, dateSelected, stopIds)

merge = [train, regTrain, tram, nightBus]
result = pd.concat(merge)
result.to_csv('data.csv')

transformedData = generateResultData(result)
transformedData.to_csv('final.csv')