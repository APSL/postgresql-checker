from functions import query
import time

n = query("SELECT * FROM elefants;").rowcount

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


