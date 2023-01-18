import os
import psycopg2
import nltk

DATABASE_URL = "postgresql://txtaquote:Y6uLs5rldEbg8cW5-BzjGg@loner-quagga-8019.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"

conn = psycopg2.connect(os.environ["DATABASE_URL"])

cur = conn.cursor()
#cur.execute("SELECT Users")

#cur.execute("CREATE TABLE test3 (data varchar);")

name = "moshe";
#cur.execute("INSERT INTO test (num,data) VALUES (%s,%s)",(100,"name")) 
cur.execute("SELECT data FROM test3;")
stuff = cur.fetchall()
num = 0
for i in stuff:
    name5 = nltk.wordpunct_tokenize(str(i))
    print(name5[1])
    if name5[1] == name:
        num += 1
if num == 0:
    cur.execute("INSERT INTO test3 (data) VALUES (%s)",(name,))

cur.execute("SELECT data FROM test3;")

print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
