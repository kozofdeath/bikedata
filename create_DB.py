import sqlite3 as lite;
import requests
import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import collections

r = requests.get('http://www.citibikenyc.com/stations/json');

#data structure
data = r.json()

#returns a dict w/ keys: [u'executionTime', u'stationBeanList']
#station is a list composed of diictionaries
keys = data.keys()
station_list_data = data[keys[1]]

key_list = [];
for station in station_list_data:
    keys = station.keys();
    for k in keys:
        if k not in key_list:
            key_list.append(k)

#staion keys: [u'availableDocks', u'totalDocks', u'city', u'altitude', u'stAddress2', u'longitude', u'lastCommunicationTime', u'postalCode', u'statusValue',
#u'testStation', u'stAddress1', u'stationName', u'landMark', u'latitude', u'statusKey', u'availableBikes', u'id', u'location']

#makes a dataframe from json data
df1 = json_normalize(r.json()['stationBeanList'])

#create bike databases
reference_ids = [u'id',
u'totalDocks',
u'city',
u'altitude',
u'stAddress2',
u'longitude',
u'postalCode',
u'testStation',
u'stAddress1',
u'stationName',
u'latitude',
u'location'
]

print reference_ids;

ref_query = """CREATE TABLE citibike_reference (id INT PRIMARY KEY, u'id',
u'totalDocks',
u'city',
u'altitude',
u'stAddress2',
u'longitude',
u'postalCode',
u'testStation',
u'stAddress1',
u'stationName',
u'latitude',
u'location')
"""

fill_ref_query = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

print ref_query;

con = lite.connect('citi_bike.db')
cur = con.cursor()
with con:
    cur.execute(ref_query)s
    for station in station_list_data:
        cur.execute(fill_ref_query, station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))


#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist();

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

#create the table
#in this case, we're concatenating the string and joining all the station ids (now with '_' and 'INT' added)
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

# a package with datetime objects
import time

# a package for parsing a string into a Python datetime object
from dateutil.parser import parse

#take the string and parse it into a Python datetime object
exec_time = parse(r.json()['executionTime'])
