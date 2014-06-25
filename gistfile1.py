import psycopg2
import time
import sys

try:
    conn = psycopg2.connect("dbname=test user=test password=12345678")
    cur = conn.cursor()
    cur.execute("DROP TABLE elefants;")
    cur.execute("CREATE TABLE elefants (id serial PRIMARY KEY, name varchar);")
    conn.commit()
    conn.close()
except:
    print "No se puede conectar a la base de datos"
    sys.exit()

n = 1
while True:
    time.sleep(1)
    try:
        conn = psycopg2.connect("dbname=test user=test password=12345678")
        cur = conn.cursor()
        cur.execute("SELECT * FROM elefants;")
        num  = cur.rowcount
        print "%s elefantes se balanceaban, como veian que no se caian," \
              " fueron a llamar a otro elefante, llamado: %d" % (num, n)
        cur.execute("INSERT INTO elefants (name) VALUES ('%d');" % n)
        conn.commit()
        conn.close()
    except:
        print "ERROR: El elefante %d se ha caido de la tela" % n
    n = n + 1