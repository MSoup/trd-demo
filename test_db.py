import unittest
import psycopg2
from db.config import config

class TestDatabase(unittest.TestCase):
    def setup(self):
        self.conn = None
        self.params = config()
        
    def test_db_connection(self):
        # connect to the PostgreSQL server
        self.conn = psycopg2.connect(**self.params)
        self.assertEqual(isinstance(self.conn, object), True)

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
