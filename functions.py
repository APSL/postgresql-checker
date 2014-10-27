import psycopg2
import yaml

def query(select, host=""):
    try:
        filename = 'config.yml'
        stream = file(filename, 'r')
        config  = yaml.load(stream)
    except:
        print "Error al configurar desde el archivo config.yml. Existe el archivo?"

    if host != "":
        config['host'] = host

    try:
        conn = psycopg2.connect("dbname=%(database)s user=%(user)s password=%(password)s host=%(host)s" % config)
        cur = conn.cursor()
        cur.execute(select)
        conn.commit()
        conn.close()
        return cur
    except:
        print "Error al ejecutar la query: '%s'" % select
        return