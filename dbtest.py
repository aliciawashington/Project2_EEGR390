import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="pi",
    password="henny")

cur = conn.cursor()

cur.execute("select name, company from people")

rows = cur.fetchall()

for r in rows:
    print(f"name {r[0]} company {r[1]}")


#Closes the connection with the database
cur.close()