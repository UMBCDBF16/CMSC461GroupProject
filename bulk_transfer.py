#name: bulk_transfer.py
#author: Grace Chandler
#date: 11-13-16
#description

#parse the csv into data 
def parse_csv(csv):
  relations = []
  data = open(csv,'r')
  
  #we are assuming tablename is the first line of the CSV
  tablename = data.readline().strip()
  
  #going through the file to split each piece of data into a list
  for line in data:
    #although the line could be left as-is to be used as the values section of a query
    #splitting it up allows for more flexiblity in manipulation and validation
    line = line.strip().split(',')
    relations.append(line)
  
  data.close()
  
  return relations,tablename

#this function creates the queries from the data
def form_queries(data,tablename): 
    query_start = "INSERT " + "INTO " + tablename + " VALUES "
    
    #add here a portion to create a format like this
    # "INSERT INTO tablename (column, names, here) VALUES (values,here)
    
    values = []
    queries = []
    #go through the lines in the data list
    for d in data:
          #for each thing in the line, do type validation and add it
        for item in d:
            values.append(item)

        #create the query string
        val_str = '(' + ' , '.join(values) + ' ); '
        query = query_start + val_str
        
        #change this to an execution of the query 
        queries.append(query)
        
        values = []
   
    return queries
  
  
def main():
  relations,tablename = parse_csv("csv.txt")
  print(tablename)
  queries = form_queries(relations,tablename)
  print(queries)
main()
  