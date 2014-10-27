import psycopg2
import time

def query(select, host):
    try:
        conn = psycopg2.connect("dbname=test user=test password=12345678 host=%s" % host)
        cur = conn.cursor()
        cur.execute("SET statement_timeout = 500;")               
        cur.execute(select)
        conn.commit()
        conn.close()
        return cur
    except:
        return

cluster = "192.168.0.100"
lohap1 = "192.168.0.1"
lohap2 = "192.168.0.2"

n = query("SELECT * FROM elefants;", cluster).rowcount

while True:
    time.sleep(1)
    try:
        num  = query("SELECT * FROM elefants;", cluster).rowcount
        print "%s elefantes se balanceaban, como veian que no se caian," \
              " fueron a llamar a otro elefante, llamado: %d" % (num, n)
        query("INSERT INTO elefants (name) VALUES ('%d');" % n, cluster)
    except:
        print "ERROR: El elefante %d se ha caido de la tela" % n
    n = n + 1


