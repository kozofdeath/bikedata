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
df2 = pd.DataFrame(station_list_data)
df = df2

## these are identical dataframes as established by code below
# print 'Rows: ', df1.shape[0]
# print 'Columns: ', df1.shape[1]
# for x in range(10):
#     for y in range(df1.shape[1]):
#         print df1.iloc[x,y] == df2.iloc[x,y]

# times = [(int(t[0]), int(t[1].split('-')[0])) for t in df['lastCommunicationTime'].iteritems()];
# time_indices = map(lambda x : x[0], filter(lambda x : x[1] < 2014, times))
# print time_indices;
# print len(df)
# for t in time_indices:
#     if t in df.index:
#         print True;
#     df = df.loc[df.index != t];
# print len(df)



times = [(t, int(t.split('-')[0])) for t in df['lastCommunicationTime']];
time_indices = map(lambda x : x[0], filter(lambda x : x[1] < 2014, times)) # 9 elements long
print len(df)
print time_indices;
print 'Original mean: ', df['availableBikes'].mean();
print df['availableBikes'].median();
print 'Updated mean: ', df[~df['lastCommunicationTime'].isin(time_indices)]['availableBikes'].mean();
print df[~df['lastCommunicationTime'].isin(time_indices)]['availableBikes'].median();
print len(df)

# df = df['']
count_dict = {}
for col in df.columns:
    count_dict[col] = collections.Counter(df[col]);

print count_dict.keys();
print count_dict['statusValue'];
print count_dict['statusKey']

df.to_csv('citi_bike.csv')

#out_of_service = [t for t in df['lastCommunicationTime']]
