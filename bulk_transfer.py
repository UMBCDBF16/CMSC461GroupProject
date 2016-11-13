#name: bulk_transfer.py
#author: Grace Chandler
#date: 11-13-16
#description

def parse_csv(csv,tablename):
  
  relations = []
  data = open(csv,'r')
  for line in data:
    line = line.strip.split(',')
    relations.append(line)
    #more things
   return relations 
    
  
  