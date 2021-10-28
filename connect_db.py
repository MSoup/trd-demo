#
# Small script to show PostgreSQL and Pyscopg together
#

# host='localhost'

import psycopg2

try:
    con = psycopg2.connect("dbname='github_actions' user='postgres' password='dbpass'")
except:
    print("I am unable to connect to the database")


cur = con.cursor()

cur.execute("CREATE DATABASE test")