import requests
import pandas as pd
from pandas.io.json import json_normalize
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

#these are identical dataframes!
df1 = json_normalize(r.json()['stationBeanList'])
df2 = pd.DataFrame(station_list_data)

# print 'Rows: ', df1.shape[0]
# print 'Columns: ', df1.shape[1]
# for x in range(10):
#     for y in range(df1.shape[1]):
#         print df1.iloc[x,y] == df2.iloc[x,y]

#pd.DataFrame({'rainy': [.4, .7], 'sunny' : [.6, .3]} , index=['rainy', 'sunny']);

#you can do len(df)
