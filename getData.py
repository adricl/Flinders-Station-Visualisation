import partridge as ptg

from collections import defaultdict
import datetime
import os
import shutil
import tempfile
from typing import DefaultDict, Dict, FrozenSet, Optional, Set, Tuple

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))


inpath = 'data/gtfs/2/google_transit.zip'
dateSelected = datetime.datetime(2019,7,20)

feed = ptg.load_raw_feed(inpath)
trips = feed.trips
stops = feed.stops
stop_times = feed.stop_times
stop_ids = stops[stops['stop_name'].str.contains('Flinders')]['stop_id']

service_id_by_selected_day = {}
service_ids_by_date = ptg.read_service_ids_by_date(inpath)
for date, service_id in service_ids_by_date.items():
  if (date == dateSelected.date()):
    service_id_by_selected_day = service_id

#we create a temp column to sort by
sort_column = []
for time in stop_times['arrival_time']:
  split = time.split(':')
  join = ''
  sort_column.append(int(join.join(split)))
stop_times['sort_column'] = sort_column



trip_ids = trips[trips.service_id.isin(service_id_by_selected_day)].trip_id
filter_by_trips = stop_times[stop_times.trip_id.isin(trip_ids)]
filter_by_stops = filter_by_trips[filter_by_trips.stop_id.isin(stop_ids)]

#Create a column to work out arival or departure 
#we assume if the stop_sequence is 1 we are departing and if its great than 1 we are just 
for row in filter_by_stops:
  print(row[4])
  #if int(row['stop_sequence']) > 1:
  #  row['direction'] = 'arrival'
  #else:
  #  row['direction'] = 'depart'

filter_by_stops_sorted = filter_by_stops.sort_values(by='sort_column', axis=0, ascending=True)
filter_by_stops_sorted.to_csv('test.csv')
#trains_per_stop = stop_times.where(filter_by_trips & filter_by_stops)
#trains_per_stop = trains_per_stop.dropna()
#print(trains_per_stop)