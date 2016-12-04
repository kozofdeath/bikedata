import sqlite3 as lite;

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

print ref_query;

con = lite.connect('citi_bike.db')
cur = con.cursor()
with con:
    cur.execute(ref_query)s
