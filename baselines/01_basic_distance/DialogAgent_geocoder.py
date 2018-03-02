import datetime
import googlemaps
import sys
import geocoder
from geojsonio import display
from shapely.geometry import Point

from geopandas import GeoDataFrame
import pandas as pd 
import geocoder 
import googlemaps
from shapely.geometry import Point
from geojsonio import display

import gmplot

class DialogAgent(object):

   def __init__(self):
       date = str(datetime.datetime.now()).split()[0]
       time = str(datetime.datetime.now()).split()[1]
       self.log_file_name = 'logs/log_' + date + '_' + time 
       self.gmaps = googlemaps.Client(key='AIzaSyCMU3s5rzipRA4lXhGT8aiBaXlPJemQLF4')

   def print_logfilename(self):     
       print self.log_file_name

   def get_gdf(self):
        crs = {'init': 'epsg:4326'}
        return(GeoDataFrame(self.get_names(), crs=crs, geometry=self.get_geo()))

       
   def visualize(self,query):
        lat, lng = self.gmaps.address_to_latlng(query)
        self.boba['Coordinates'] = [Point(lng,lat)]
        updated = self.get_gdf()
        display(updated.to_json())
 
   def start_chat(self):
       f = open(self.log_file_name, 'w')
       greeting = 'Hello. Where do you want to go today?'
       f.write("Bot: " + greeting + '\n')
       print greeting 
       query = str(raw_input())
       f.write("user: " +  query)
       print "Okay I think you said ", query
       # Check number of places
       #num_places = get_numplaces(query)
       time_to_travel = self.get_distance(query)
       print "I think it will take you: ", time_to_travel 
       gmap = gmplot.GoogleMapPlotter.from_geocode(query)
       gmap.draw("map.html")
       print "I have put a map for you in map.html"


   def get_distance(self, query):
       now = datetime.datetime.now()
       directions_result = self.gmaps.directions("Pittsburgh", query, mode='transit', departure_time=now)
       try:
         res = directions_result[0]
         for s in res['legs']:
            return s['duration']['text']
       except IndexError:
            print "Hmm. I dont know the answer to that. Sorry"
            print "I am easily confused. Can you be more specific"
            query = str(raw_input())
            return self.get_distance(query)           

DA = DialogAgent()
#DA.print_logfilename()
DA.start_chat()
