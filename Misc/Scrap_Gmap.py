# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:42:25 2020

@author: yp229
"""
# Referred from https://towardsdatascience.com/foods-around-me-google-maps-data-scraping-with-python-google-colab-588986c63db3


import pandas as pd
import numpy as np
import requests
import json
import time
final_data = []
# Parameters
coordinates = ['12.978944, 77.768151']          #your location

keywords = ['Grocery']                          #your key word - what you want to search on maps

radius = '1000'                                 #How much radius : Keep in mind that google allows scrapping only 60 top results /  it shows only 60 results

api_key = 'AIzaSyB3vSNv7cnsJt5q-iadmumuR7FOtMOh8rI' #insert your Places API

for coordinate in coordinates:
    for keyword in keywords:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinate+'&radius='+str(radius)+'&keyword='+str(keyword)+'&key='+str(api_key)
        while True:
            print(url)
            respon = requests.get(url)
            jj = json.loads(respon.text)
            results = jj['results']
            for result in results:
                name = result['name']
                place_id = result ['place_id']
                lat = result['geometry']['location']['lat']
                lng = result['geometry']['location']['lng']
                rating = result['rating']
                types = result['types']
                vicinity = result['vicinity']
                data = [name, place_id, lat, lng, rating, types, vicinity]
                final_data.append(data)
                time.sleep(5)
            if 'next_page_token' not in jj:
                break
            else:
                next_page_token = jj['next_page_token']
                url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key='+str(api_key)+'&pagetoken='+str(next_page_token)
labels = ['Place Name','Place ID', 'Latitude', 'Longitude', 'Rating','Types', 'Vicinity']
export_dataframe_1_medium = pd.DataFrame.from_records(final_data, columns=labels)
export_dataframe_1_medium.to_csv('Scrapped_data_Map.csv')

