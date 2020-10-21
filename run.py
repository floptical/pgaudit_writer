#!/root/pgaudit_writer/venv/bin/python
import psycopg2

conn = psycopg2.connect(host="localhost",user="postgres")

cur = conn.cursor()
cur.execute("""SELECT 1""")
rows = cur.fetchall()
print(rows)
