from functions import query

query("DROP TABLE elefants;")
query("CREATE TABLE elefants (id serial PRIMARY KEY, name varchar);")

