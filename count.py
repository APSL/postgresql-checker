from functions import query
import time

n = query("SELECT * FROM elefants;").rowcount
print "Hay %s elefantes en la tela" % n
