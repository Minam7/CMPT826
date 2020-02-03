import os

import folium
import pandas as pd
from folium.plugins import HeatMap

print('start-----------')
# plotting heatmap for all records
gps_data = pd.read_pickle('data/gps.pkl')
print('reading data')
# creating map
hmap_data = folium.Map(location=[52.058367, -106.7649138128])
print('creating map')
for lat, lon in zip(gps_data['lat'], gps_data['lon']):
    folium.Marker([lat, lon]).add_to(hmap_data)
print('adding marker to map')
sw = gps_data[['lat', 'lon']].min().values.tolist()
print('find min')
ne = gps_data[['lat', 'lon']].max().values.tolist()
print('find max')
hmap_data.fit_bounds([sw, ne]) 
print('fit done')
hm_wide = HeatMap(list(zip(gps_data.lat.values, gps_data.lon.values, )), min_opacity=0.2)
print('add heatmap data')
hmap_data.add_child(hm_wide)
print('heatmap added to map')
hmap_data.save(os.path.join('maps', 'all_data_heatmap.html'))
print('saving dons')