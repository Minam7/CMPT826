import pandas as pd

# reading data from pickle object
battery_data = pd.read_pickle('data/battery.pkl')

############################################################
'''
Part A: removing users with 50% and 75% battery records
'''
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

############################################################
'''
Part B: removing GPS data outside of Saskatoon
'''
