import pandas as pd

# retrieving saskatoon data with less than 100m accuracy
gps_data = pd.read_pickle('data/gps_filter.pkl')

# retrieving users with more than 50% battery info
user_battery = pd.read_pickle('data/battery_50.pkl')

# creating dataframe for filtering Saskatoon data for preferred users
good_user_id = user_battery.user_id.unique()
gps_data = gps_data[gps_data.user_id.isin(good_user_id)]

# now we have 5676081 records.