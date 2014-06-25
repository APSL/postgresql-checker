import psycopg2
import time

def query(select):
    try:
        conn = psycopg2.connect("dbname=test user=test password=12345678")
        cur = conn.cursor()
        cur.execute(select)
        conn.commit()
        conn.close()
        return cur
    except:
        return

query("DROP TABLE elefants;")
query("CREATE TABLE elefants (id serial PRIMARY KEY, name varchar);")

n = 1

while True:
    time.sleep(1)
    try:
        num  = query("SELECT * FROM elefants;").rowcount
        print "%s elefantes se balanceaban, como veian que no se caian," \
              " fueron a llamar a otro elefante, llamado: %d" % (num, n)
        query("INSERT INTO elefants (name) VALUES ('%d');" % n)
    except:
        print "ERROR: El elefante %d se ha caido de la tela" % n
    n = n + 1