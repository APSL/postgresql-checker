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
        num1  = query("SELECT * FROM elefants;", lohap1).rowcount
    except:
        num1 = 0
    try:
        num2  = query("SELECT * FROM elefants;", lohap2).rowcount
    except:
        num2 = 0
    print "LOHAP1 %d -- %d LOHAP2" % (num1, num2)
