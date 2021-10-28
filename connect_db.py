#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='dbpass'")
except:
    print("I am unable to connect to the database")


cur.conn.cursor()

cur.execute("CREATE DATABASE test")