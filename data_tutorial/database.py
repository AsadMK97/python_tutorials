import psycopg2
import psycopg2.extras


try:
    conn = psycopg2.connect("dbname='weather' user='postgres' password='ferrari786'")
except:
    print("I am unable to connect to the database.")


cur = conn.cursor()
try:
    cur.execute("""SELECT * from weather""")
except:
    print("I can't SELECT from weather")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print("   "), row[1]
