# Small script to show PostgreSQL and Pyscopg together
#

# 

import psycopg2

try:
    con = psycopg2.connect("dbname='github_actions' host='localhost' user='postgres' password='dbpass'")
    cur = con.cursor()
    cur.execute("CREATE DATABASE test")
except:
    print("I am unable to connect to the database")