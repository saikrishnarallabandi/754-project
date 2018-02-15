import datetime

class DialogAgent(object):

    def __init__(self):
       date = str(datetime.datetime.now()).split()[0]
       time = str(datetime.datetime.now()).split()[1]
       self.log_file_name = 'logs/log_' + date + '_' + time 

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

DA = DialogAgent()
#DA.print_logfilename()
DA.start_chat()
