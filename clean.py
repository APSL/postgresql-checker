import psycopg2
import time

def query(select, host):
    try:
        conn = psycopg2.connect("dbname=test user=test password=12345678 host=%s" % host)
        cur = conn.cursor()
        cur.execute(select)
        conn.commit()
        conn.close()
        return cur
    except:
        return

cluster = "192.168.0.100"
lohap1 = "192.168.0.1"
lohap2 = "192.168.0.2"

query("DROP TABLE elefants;", cluster)
query("CREATE TABLE elefants (id serial PRIMARY KEY, name varchar);", cluster)

