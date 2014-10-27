from functions import query
import time

cluster = "192.168.0.100"
nodo1 = "192.168.0.1"
nodo2 = "192.168.0.2"

n = query("SELECT * FROM elefants;", cluster).rowcount

while True:
    time.sleep(1)
    try:
        num1  = query("SELECT * FROM elefants;", nodo1).rowcount
    except:
        num1 = 0
    try:
        num2  = query("SELECT * FROM elefants;", nodo2).rowcount
    except:
        num2 = 0
    print "NODO1 %d -- %d NODO2" % (num1, num2)
