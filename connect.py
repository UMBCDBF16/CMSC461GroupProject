import sqlite3

#this function will always return a valid connection object to a sqlite3 database
def getConnection():
  conn=sqlite3.connect(":memory:")
  return conn