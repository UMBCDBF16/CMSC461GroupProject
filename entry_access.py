#name: entry_access.py
#author: Katelyn Seitz
#date: 12-01-16
#description: defines update , delete, and select

import sqlite3
DB_CONN = sqlite3.connect("UMBC.db")
DB_CURSOR = DB_CONN.cursor()

def col_names(table):
  DB_CURSOR.execute("select * from {tbl}".\
    format(tbl = table))
  return [member[0] for member in DB_CURSOR.description]

#COMPLETE   
def update(table):
  '''
  adds a new record to table
  '''
  fields = tuple(col_names(table))
  print(table, "contains these fields: ", fields)
  entry = input("Please enter all values for new entry (separated by ',') ")
  values = tuple([x.strip() for x in entry.split(',')])
  try:
    query = "INSERT INTO " + table + str(fields) + " VALUES " + str(values)  
    DB_CURSOR.execute(query)
  except sqlite3.IntegrityError:
    print("ERROR: ID already exists in PRIMARY KEY column ", str(fields))
  

#COMPLETE   
def delete_relation(table):
  '''
  Prompts user WHERE clause(s) which are then used
  to delete records. entering 'NULL' for WHERE clause removes all 
  entries, but not the table itself.
  '''  
  headers = ', '.join(col_names(table))
  print(table, "contains these fields: ", headers)
  condition = input("Please enter a condition ('NULL' to delete all entries) ")
  if condition == "NULL":
    query = "DELETE FROM " + table  
  else:
    query = 'DELETE FROM ' + table + ' WHERE ' + condition
  DB_CURSOR.execute(query)

#COMPLETE
def select(table):
  '''
  Prompts user for field(s) and optional WHERE clause(s) which are then used
  to print out records.  
  '''
  headers = ', '.join(col_names(table))
  print(table, "contains these fields: ", headers)
  fields = input("Please enter the fields you wish to select (separated by ',') ")
  condition = input("Please enter a condition ('NULL' to ommit WHERE clause) ")
  if condition == "NULL":
    query = "SELECT " + fields + " FROM " + table    
  else:
    query = 'SELECT '+ fields +' FROM ' + table + ' WHERE ' + condition
  DB_CURSOR.execute(query)
  print(DB_CURSOR.fetchall())

  
  
