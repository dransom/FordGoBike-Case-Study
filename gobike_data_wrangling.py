"""
Script with all the data wrangling of the Ford GoBike data set.
Returns two DataFrames: 
- bikes: all the information pertaining to each bike ride
- stations: station specific information (id, name, log, lat)
"""

import numpy as np
import pandas as pd

def gobike_data():
   
    # Read in file & print first few statements
    bikes = pd.read_csv('201902-fordgobike-tripdata.csv')

    # Issue #1 start_time & end_time conversion
    bikes['start_time'] = pd.to_datetime(bikes.start_time)
    bikes['end_time'] = pd.to_datetime(bikes.end_time)

    # Issue #2 start_station_id & end_station_id conversion
    bikes['start_station_id'] = bikes.start_station_id.astype(str).str.replace('.0', '', regex = False)
    bikes['end_station_id'] = bikes.end_station_id.astype(str).str.replace('.0', '', regex = False)

    # Issue #3 bike_id
    bikes['bike_id'] = bikes.bike_id.astype(str)

    # Issue #4: member_gender
    gender_list = ['Male', 'Female', 'Other']
    gender_cat_type = pd.api.types.CategoricalDtype(categories = gender_list, ordered = False)
    bikes['member_gender'] = bikes.member_gender.astype(gender_cat_type)

    # Issue #5: user_type conversion
    user_list = ['Subscriber', 'Customer']
    user_cat_type = pd.api.types.CategoricalDtype(categories = user_list, ordered = False)
    bikes['user_type'] = bikes.user_type.astype(user_cat_type)

    # Issue #6: member_birth_year conversion
    bikes['member_birth_year'] = bikes.member_birth_year.astype('Int64')

    # Issue #7: data tidiness

    # Seperate start and end stations
    start_stations = bikes[['start_station_id','start_station_name', 'start_station_longitude', 'start_station_latitude']].copy()
    end_stations = bikes[['end_station_id', 'end_station_name', 'end_station_longitude', 'end_station_latitude']].copy()

    # Rename columns
    start_stations.rename(columns = {'start_station_id': 'id', 
                                    'start_station_name': 'name', 
                                    'start_station_longitude': 'longitude',
                                    'start_station_latitude': 'latitude'},
                        inplace = True)
    end_stations.rename(columns = {'end_station_id': 'id',
                                'end_station_name': 'name',
                                'end_station_longitude': 'longitude',
                                'end_station_latitude': 'latitude'},
                    inplace = True)

    # Drop any duplicates
    start_stations.drop_duplicates(subset = 'id', inplace = True)
    end_stations.drop_duplicates(subset = 'id', inplace = True)

    # Merge two DFs together to form one for stations
    stations = pd.merge(start_stations, end_stations, on = ['id', 'name', 'longitude', 'latitude'], how = 'outer')

    # Drop any remaining duplicates
    stations.drop_duplicates(subset = 'id', inplace = True)

    # Drop extra station columns
    bikes.drop(['start_station_name', 'start_station_longitude', 'start_station_latitude',
           'end_station_name', 'end_station_longitude', 'end_station_latitude'], 
          axis = 1,
          inplace = True)

    # Write files with corrected data
    bikes.to_csv('gobike-rides-master.csv')
    stations.to_csv('gobike-stations-master.csv')

    return bikes, stations