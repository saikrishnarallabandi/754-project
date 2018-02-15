import datetime
import googlemaps
import sys

class DialogAgent(object):

    def __init__(self):
       date = str(datetime.datetime.now()).split()[0]
       time = str(datetime.datetime.now()).split()[1]
       self.log_file_name = 'logs/log_' + date + '_' + time 
       self.gmaps = googlemaps.Client(key='AIzaSyCMU3s5rzipRA4lXhGT8aiBaXlPJemQLF4')

    def print_logfilename(self):     
       print self.log_file_name

    def start_chat(self):
       f = open(self.log_file_name, 'w')
       greeting = 'Hello. Where do you want to go today?'
       f.write("Bot: " + greeting + '\n')
       print greeting 
       query = str(raw_input())
       f.write("user: " +  query)
       print "Okay I think you said ", query
       time_to_travel = self.get_distance(query)
       print "I think it will take you: ", time_to_travel 

    def get_distance(self, query):
       now = datetime.datetime.now()
       directions_result = self.gmaps.directions("Pittsburgh", query, mode='transit', departure_time=now)
       try:
         res = directions_result[0]
         for s in res['legs']:
            return s['duration']['text']
       except IndexError:
            print "Hmm. I dont know the answer to that. Sorry"
            sys.exit()
           
DA = DialogAgent()
#DA.print_logfilename()
DA.start_chat()
