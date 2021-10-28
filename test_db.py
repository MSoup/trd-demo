import unittest
import sys
import psycopg2
from db.config import config

class TestDatabase(unittest.TestCase):
    def test_db_connection(self):
        conn = None
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        print(conn)

# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
		
#         # create a cursor
#         cur = conn.cursor()
        
# 	# execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')

# 	# close the communication with the PostgreSQL
#         cur.close()

#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')
