# CMSC461GroupProject
Group project for Fall 2016 Database class at UMBC

Build Instructions:
Run main.py
No external connections or internal databases are needed as this is run on a RAM Database.
However, this also means that the database is not persistant between runs.
Script to create the schema is automatically run when the program is opened without user interaction.
The user is not given control over the schema that is run in the database.
Forign keys can be turned on by uncommenting the "pragma" line: disabled for ease of loading
tables into database through csv in any order.

*********

Input:
Format for the csv files  
line 1: tablename  
other lines: attributes,separated,by,commas

NOTE: Please make sure that there are not extraneous punctuation marks, especially apostrophes(') in this file

Descriptions of files in the repo:



Notes on Functions (write something about each one):
***Hey guys, so if you could write about the functions you helped write, and a brief methodology about why you did it the way you did that would be great***

bulk_load: This function reads in a csv and constructs sql commands to insert large amounts of data at the time into a table.
To accomplish this task, basic Python string manipulation techniques were exploited, notably splicing lines at commas, stripping whitespace,
and reconstructing strings in given patterns.

erase: This erases all entries in the selected table
delete: This erases entries conditionaly based on input
...
...
...
