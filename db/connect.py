#!/usr/bin/python
# import psycopg2
# from config import config

# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
#         print(conn)
#         print(type(conn))
#         # create a cursor
#         cur = conn.cursor()
#         print(cur)
#         print(type(cur))
        
# 	# execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')

#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)
       
#         print('Creating DB contents...')
#         cur.execute("CREATE TABLE test_db (id serial PRIMARY KEY, num integer, data varchar);")

#         print("Select table that I made")
#         cur.execute("INSERT INTO test_db (num, data) VALUES (%s, %s)",(100, "abc'def"))

#         print("Test to see if DB retrieves it")
#         cur.execute("SELECT * FROM test_db;")

#         fetched_data = cur.fetchone()
#         print(fetched_data)
# 	# close the communication with the PostgreSQL
#         cur.close()

#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


# if __name__ == '__main__':
#     connect()