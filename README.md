# CMSC461GroupProject
Group project for Fall 2016 Database class at UMBC

###Build Instructions:
Run main.py

No external connections or internal databases are needed as this is run on a RAM Database.
However, this also means that the database is not persistant between runs.
Script to create the schema is automatically run when the program is opened without user interaction.
The user is not given control over the schema that is run in the database.
Forign keys can be turned on by uncommenting the "pragma" line: disabled for ease of loading
tables into database through csv in any order.

*********

###Format for the csv files  
**line 1**: tablename  
**other lines**: attributes,separated,by,commas

NOTE: Please make sure that there are not extraneous punctuation marks, especially apostrophes(') in this file, and that non-numeric data is encased in single quotes (This includes dates).

###Notes on Functions:

**bulk_load**: This function reads in a csv and constructs sql commands to insert large amounts of data at the time into a table.
To accomplish this task, basic Python string manipulation techniques were exploited, notably splicing lines at commas, stripping whitespace, and reconstructing strings in given patterns.

**erase**: This erases all entries from the selected table.

**delete**: This deletes entries that match the given condition.

**select**: Returns a list of entries that match the given condition.

**insert**: Guides the user to add an entry to the chosen table.
