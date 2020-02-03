import pandas as pd
import sqlalchemy as db

engine = db.create_engine('mysql://sem311:p^HA89/h@crepe.usask.ca:3306/SHED10')

connection = engine.connect()
metadata = db.MetaData()

'''

Obtaining battery table

# Equivalent to 'SELECT * FROM battery
battery = db.Table('battery', metadata, autoload=True, autoload_with=engine)
query = db.select([battery])

# getting data by executing the query above
BatteryResultProxy = connection.execute(query)
BatteryResultSet = BatteryResultProxy.fetchall()

# converting data to data frame
battery_data = pd.DataFrame(BatteryResultSet)
battery_data.columns = BatteryResultSet[0].keys()

# removing index column from data - 0 for rows and 1 for column
battery_data = battery_data.drop('index', 1)

# saving data frame as pickle object for future use
battery_data.to_pickle('data/battery.pkl')

print('fetching battery data completed')

'''

'''
Obtaining gps table
'''
# Equivalent to 'SELECT * FROM gps
gps = db.Table('gps', metadata, autoload=True, autoload_with=engine)
query = db.select([gps])

# getting data by executing the query above
GPSResultProxy = connection.execute(query)
GPSResultSet = GPSResultProxy.fetchall()

# converting data to data frame
gps_data = pd.DataFrame(GPSResultSet)
gps_data.columns = GPSResultSet[0].keys()

# removing index column from data - 0 for rows and 1 for column
gps_data = gps_data.drop('index', 1)

# saving data frame as pickle object for future use
gps_data.to_pickle('data/gps.pkl')

print('fetching gps data completed')
