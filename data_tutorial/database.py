#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2


# Connect to your postgres DB
conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM my_data")

# Retrieve query results
records = cur.fetchall()