import os

import folium
import pandas as pd
from folium.plugins import HeatMap

'''
Part A: removing users with 50% and 75% battery records
'''

# reading data from pickle object
battery_data = pd.read_pickle('data/battery.pkl')

# counting number of battery information per user
battery_info = battery_data.groupby(['user_id']).size().reset_index(name='record_count')

# finding number of users before filtering
all_users, _ = battery_info.shape
print('There is a total of', all_users, 'users.')

'''
50%
'''

# calculating filtering cutoff
cutoff_percentage = 0.5
max_battery_info = (60 / 5) * 24 * 30
battery_cutoff = cutoff_percentage * max_battery_info

# filtering users with less than 50%
battery_info_50 = battery_info.loc[battery_info['record_count'] > battery_cutoff]
users_filter_50, _ = battery_info_50.shape

# preserving only users with more than 50% battery record
battery_data_50 = pd.merge(left=battery_data, right=battery_info_50, left_on='user_id', right_on='user_id')

print(all_users - users_filter_50, 'users are removed in 50% threshold.')

'''
75%
'''

# calculating filtering cutoff
cutoff_percentage = 0.75
battery_cutoff = cutoff_percentage * max_battery_info

# filtering users with less than 75%
battery_info_75 = battery_info.loc[battery_info['record_count'] > battery_cutoff]
users_filter_75, _ = battery_info_75.shape

# preserving only users with more than 75% battery record
battery_data_75 = pd.merge(left=battery_data, right=battery_info_75, left_on='user_id', right_on='user_id')

print(all_users - users_filter_75, 'users are removed in 75% threshold.')

# saving data frame as pickle object for future use
battery_data_50.to_pickle('data/battery_50.pkl')
battery_data_75.to_pickle('data/battery_75.pkl')

############################################################

'''
Part B: removing GPS data outside of Saskatoon
'''

# reading data from pickle object
gps_data = pd.read_pickle('data/gps.pkl')

# finding number of all records
records_num, _ = gps_data.shape
print('There is a total of', records_num, 'GPS record.')

'''
Accuracy filtering
'''

# filtering accuracy more than 100
gps_data_filter_acc = gps_data.loc[gps_data['accu'] < 100]
gps_filter_accu, _ = gps_data_filter_acc.shape

print(records_num - gps_filter_accu, 'records are removed for accuracies more than 100m.')

'''
Latitude filtering
'''

# outside latitude range
gps_data_filter_lat = gps_data.loc[gps_data['lat'] > 52.058366]
gps_filter_lat_low, _ = gps_data_filter_lat.shape

print(records_num - gps_filter_lat_low, 'records are removed for latitudes less than 52.058367')

gps_data_filter_lat = gps_data_filter_lat.loc[gps_data_filter_lat['lat'] < 52.214609]
gps_filter_lat_high, _ = gps_data_filter_lat.shape

print(records_num - gps_filter_lat_high, 'records are removed for latitudes more than 52.214608')

'''
Longitude filtering
'''

# outside longitude range
gps_data_filter_lon = gps_data[gps_data['lon'] > -106.7649138128]
gps_filter_lon_low, _ = gps_data_filter_lon.shape

print(records_num - gps_filter_lon_low, 'records are removed for longitudes less -106.7649138128')

gps_data_filter_lon = gps_data_filter_lon.loc[gps_data_filter_lon['lon'] < -106.52225319]
gps_filter_lon_high, _ = gps_data_filter_lon.shape

print(records_num - gps_filter_lon_high, 'records are removed for latitudes more than -106.52225318')

############################################################
# executing all filters to a final data frame
gps_data = gps_data.loc[gps_data['accu'] < 100]
gps_data = gps_data.loc[gps_data['lat'] > 52.058366]
gps_data = gps_data.loc[gps_data['lat'] < 52.214609]
gps_data = gps_data[gps_data['lon'] > -106.7649138128]
gps_data = gps_data.loc[gps_data['lon'] < -106.52225319]

records_num, _ = gps_data.shape

print('GPS data size after filtering is', records_num, 'records.')

# saving data frame as pickle object for future use
gps_data.to_pickle('data/gps_filter.pkl')

############################################################

'''
Part C: plotting
'''

# plotting heatmap for all records
gps_data = pd.read_pickle('data/gps.pkl')

# creating map
hmap_data = folium.Map(location=[52.058367, -106.7649138128])

hm_wide = HeatMap(list(zip(gps_data.lat.values, gps_data.lon.values, )), min_opacity=0.2)

hmap_data.add_child(hm_wide)

hmap_data.save(os.path.join('maps', 'all_records_heatmap.html'))

# plotting heatmap for filtered records
gps_data = pd.read_pickle('data/gps_filter.pkl')

# creating map
hmap_data = folium.Map(location=[52.058367, -106.7649138128])

hm_wide = HeatMap(list(zip(gps_data.lat.values, gps_data.lon.values)), min_opacity=0.2)

hmap_data.add_child(hm_wide)

hmap_data.save(os.path.join('maps', 'filtered_records_heatmap.html'))
