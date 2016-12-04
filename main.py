import sqlite3


class DBConnection():
    def __init__(self):
        self.DB_CONN = self.get_connection()
        self.DB_CURSOR = self.DB_CONN.cursor()

    def get_connection(self):
        """
        :return: a valid connection object to a sqlite3 database
        """
        conn = sqlite3.connect(":memory:")
        return conn

    # parse the csv into data
    def parse_csv(self, csv):
        relations = []
        data = open(csv, 'r')

        # we are assuming tablename is the first line of the CSV
        tablename = data.readline().strip()

        # going through the file to split each piece of data into a list
        for line in data:
            # although the line could be left as-is to be used as the values section of a query
            # splitting it up allows for more flexiblity in manipulation and validation
            line = line.strip().split(',')
            relations.append(line)

        data.close()

        return relations, tablename


    # this function creates the queries from the data
    def form_queries(self, data, tablename):
        query_start = "INSERT " + "INTO " + tablename + " VALUES "

        # add here a portion to create a format like this
        # "INSERT INTO tablename (column, names, here) VALUES (values,here)

        values = []
        queries = []
        # go through the lines in the data list
        for d in data:
            # for each thing in the line, do type validation and add it
            for item in d:
                values.append(item)

            # create the query string
            val_str = '(' + ' , '.join(values) + ' ); '
            query = query_start + val_str

            # change this to an execution of the query
            queries.append(query)

            values = []

        return queries

    def bulk_load(self, csv_file):
        relations, tablename = self.parse_csv(csv_file)
        queries = self.form_queries(relations, tablename)
        for query in queries:
            self.DB_CURSOR.execute(query)


    def erase(self, table):
        """
        Deletes all records from table
        Does not delete the tables schemea
        input: string
        output: None
        """
        self.DB_CURSOR.execute("DELETE * FROM ?;", table)

    def list_all_tables(self):
        self.DB_CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(self.DB_CURSOR.fetchall())

    def col_names(self, table):
        self.DB_CURSOR.execute("select * from {tbl}". format(tbl=table))
        return [member[0] for member in self.DB_CURSOR.description]

    def update(self, table):
        '''
        adds a new record to table
        '''
        print(table)
        fields = tuple(self.col_names(table))
        print(table, "contains these fields: ", fields)
        entry = input("Please enter all values for new entry (separated by ',') ")
        values = tuple([x.strip() for x in entry.split(',')])
        try:
            query = "INSERT INTO " + table + str(fields) + " VALUES " + str(values)
            self.DB_CURSOR.execute(query)
        except sqlite3.IntegrityError:
            print("ERROR: ID already exists in PRIMARY KEY column ", str(fields))

    def delete_relation(self, table):
        '''
        Prompts user WHERE clause(s) which are then used
        to delete records. entering 'NULL' for WHERE clause removes all
        entries, but not the table itself.
        '''
        headers = ', '.join(self.col_names(table))
        print(table, "contains these fields: ", headers)
        condition = input("Please enter a condition ('NULL' to delete all entries) ")
        if condition == "NULL":
            query = "DELETE FROM " + table
        else:
            query = 'DELETE FROM ' + table + ' WHERE ' + condition
        self.DB_CURSOR.execute(query)

        # COMPLETE

    def select(self, table):
        '''
        Prompts user for field(s) and optional WHERE clause(s) which are then used
        to print out records.
        '''
        headers = ', '.join(self.col_names(table))
        print(table, "contains these fields: ", headers)
        fields = input("Please enter the fields you wish to select (separated by ',') ")
        condition = input("Please enter a condition ('NULL' to ommit WHERE clause) ")
        if condition == "NULL":
            query = "SELECT " + fields + " FROM " + table
        else:
            query = 'SELECT ' + fields + ' FROM ' + table + ' WHERE ' + condition
        self.DB_CURSOR.execute(query)
        print(self.DB_CURSOR.fetchall())



class ResponseHandler():
    """
    Handles input given by the user and directs them to appropriate database commands
    """
    def __init__(self):
        self.db_conn = DBConnection()

    def user_select_table(self, command):
        self.db_conn.list_all_tables()
        table = input("Select the table that you would like to ", command)
        return table

    def respond_to(self, response):
        """
        Meant to handle the different responses possible and send their data to the correct input functions
        input: string
        output: None
        """
        if response == "select":
            table = self.user_select_table("select from")
            self.db_conn.select(table)
        elif response == "update":
            table = self.user_select_table("update")
            self.db_conn.update(table)
        elif response == "delete":
            table = self.user_select_table("delete from")
            self.db_conn.delete_relation(table)
        elif response == "erase":
            table = self.user_select_table("erase")
            self.db_conn.erase(table)
        elif response == "bulk load":
            csv_file = input("Enter the csv file you would like to load")
            self.db_conn.bulk_load(csv_file)


def main():
    response_handler = ResponseHandler()
    response = input("You can update, delete, select, erase, bulk load, or quit\n")
    while response != "quit":
        response_handler.respond_to(response)
        response = input("You can update, delete, select, erase, bulk load, or quit\n")
    print("Thank you for using the database")

main()
