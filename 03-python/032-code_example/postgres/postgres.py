import warnings

warnings.filterwarnings('ignore')
import pandas as pd
import psycopg2
from psycopg2 import Error, OperationalError
import csv
from io import StringIO
from sys import exit


class postgresQuery:
    """
    ## Description:
    postgres Class
    Initiate the connection to the specify postgres database

    ## Attributes:
    `host`: hostname of the database's server

    `port`: listening port of the database (pg default 5432)

    `dbname`: database name

    `username`: Database's username

    `password`: Database's password

    `logger`: configured logging.getLogger

    `conn_string`: Connection string (containing all previous informations)
    
    ## Methods: 
    *query_db(query):*  
             Send Query to the database

    *load_data(table):*
             Load Data from table

    *create_table(df, table):*
            Create a new table and insert data from dataframe

    *drop_table(table):*
            Delete an existing table by it's name

    *delete_row(sql_delete_query):*
            Delete an existing row by a specific query


    """
    def __init__(self, hostname, port, dbname, username, password, logger):
        """
        ### Description:
        Constructs all the necessary attributes for PostrgresQuery
        
        ### Parameters: 
        `hostname`: hostname of the database's server

        `port`: listening port of the database (pg default 5432)

        `dbname`: database name

        `username`: Database's username

        `password`: Database's password

        `logger`: configured logging.getLogger

        """
        self.host = hostname
        self.port = port
        self.dbname = dbname
        self.user = username
        self.password = password
        self.logger = logger
        self.logger.info("__init__, param : {}".format({"hostname": hostname, "port": port, "dbname": dbname,
                                                        "username": username, "password": "*******"}))
        self.conn_string = "host={} port={} dbname={} user={} password={}".format(self.host, self.port,
                                                                                       self.dbname, self.user,
                                                                                       self.password)
        
    def query_db(self, query):
        """
        ### Description:
        Send Query to the database 
        
        ### Args:
        `query`: String - Postgres Query 
        
        ### Returns: 
        `data`: pandas.DataFrame of the results 
        
        #### [DEBUG]
        shape of the received dataframe 
        
        if connection failed  
        `Connection to databse failed`
        """
        self.logger.info("query_db, param : {}".format(query))
        # Set up a connection to the postgres server.
        try:
            conn = psycopg2.connect(self.conn_string)
            self.logger.info("Connected to database !")

            # Create a cursor object
            cursor = conn.cursor()

            # Load the data
            data = pd.read_sql(query, conn)

            self.logger.debug(data.shape)
            return data
        except OperationalError as er:
            self.logger.debug("Connection to databse failed")
            self.logger.warning(er)
            exit("Can't connect to database {}, on host {}:{}".format(self.dbname, self.host, self.port))


    def load_data(self, table):
        """
        ### Description:
        Load Data from table
        Send `SELECT * FROM {table}` to the database and get a dataframe of the result

        ### Args:
        `table`: string Table name

        #### [DEBUG]
         shape of the received dataframe

        if connection failed
        `Connection to databse failed`
        """
        self.logger.info("load_data, param : {}".format(table))
        # Set up a connection to the postgres server.
        try:
            conn = psycopg2.connect(self.conn_string)
            self.logger.info("Connected to database !")

            # Create a cursor object
            cursor = conn.cursor()

            sql_command = "SELECT * FROM {};".format(str(table))
            self.logger.debug(sql_command)

            # Load the data
            data = pd.read_sql(sql_command, conn)

            self.logger.debug(data.shape)
            return data
        except OperationalError as er:
            self.logger.debug("Connection to database failed")
            self.logger.warning(er)
            exit("Can't connect to database {}, on host {}:{}".format(self.dbname, self.host, self.port))

    
    def create_table(self, df, table):
        """
        ### Description:
        Create a new table and insert data from dataframe

        ### Args:
        `df`: pandas.DataFrame Data to insert in the database

        `table`: String - Table name


        """
        self.logger.info("create_table, param : {}".format({"df": df, "table": table}))
        def psql_insert_copy(table, conn, keys, data_iter):
    
            # gets a DBAPI connection that can provide a cursor
            dbapi_conn = conn.connection
            with dbapi_conn.cursor() as cur:
                s_buf = StringIO()
                writer = csv.writer(s_buf)
                writer.writerows(data_iter)
                s_buf.seek(0)
    
                columns = ', '.join('"{}"'.format(k) for k in keys)
                if table.schema:
                    table_name = '{}.{}'.format(table.schema, table.name)
                else:
                    table_name = table.name
    
                sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
                    table_name, columns)
                cur.copy_expert(sql=sql, file=s_buf)
    
        engine = None
        df.to_sql(table, engine, method=psql_insert_copy, if_exists='replace')
    
        self.logger.info("Table : " + table + " created successfully")
    
    
    def drop_table(self, table):
        """
        ### Description:
        Delete an existing table by it's name

        ### Args:
        `table`: String - Table name

        #### [DEBUG]
        Connection to database failed
        """
        self.logger.info("drop_table, param : {}".format({"table": table}))

        try:
    
            # Set up a connection to the postgres server.
            conn = psycopg2.connect(self.conn_string)
            self.logger.info("Connected to database !")
    
            # Create a cursor object
            cursor = conn.cursor()
    
            # Form the SQL statement - DROP TABLE
            dropTableStmt = "DROP TABLE %s;" % table;
    
            # Execute the drop table command 
            cursor.execute(dropTableStmt)
    
            conn.commit()
            self.logger.info("Table droped successfully in PostgreSQL ")
    
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.debug("Connection to database failed")
            self.logger.warning("Error while creating PostgreSQL table", error)
        finally:
            # closing database connection.
            if conn:
                cursor.close()
                conn.close()
                self.logger.info("PostgreSQL connection is closed")
    
    
    def delete_row(self, sql_delete_query):
        """
        ### Description:
        Delete an existing row by a specific query

        ### Args:
        `sql_delete_query`: String - delete Query

        #### [DEBUG]
        Connection to database failed
        """
        self.logger.info("delete_row, param : {}".format({"sql_delete_query": sql_delete_query}))
        try:
            # Set up a connection to the postgres server.
            conn = psycopg2.connect(self.conn_string)
            self.logger.info("Connected to database !")

            cursor = conn.cursor()
    
            # Update single record now
            cursor.execute(sql_delete_query)
            conn.commit()
            count = cursor.rowcount
            self.logger.info(count, "Record deleted successfully ")
    
        except (Exception, psycopg2.Error) as error:
            self.logger.warning("Error in Delete operation", error)
            self.logger.debug("Connection to database failed")

        finally:
            # closing database connection.
            if (conn):
                cursor.close()
                conn.close()
                self.logger.info("PostgreSQL connection is closed")
    
    
    def insert_row(self, df, table):
        """
        ### Description:
        Insert data into an existing table from dataframe

        ### Args:
        `df`: pandas.DataFrame Data to insert in the database

        `table`: String - Table name


        """
        self.logger.info("insert_row, param : {}".format({"df": df, "table": table}))

        engine = None #TODO define the engine
        df.to_sql(table, engine, if_exists='append', index=False)
