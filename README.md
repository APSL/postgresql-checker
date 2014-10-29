postgresql-checker
==================

Dependencias:
 ```
aptitude install postgresql-server-dev-9.3 python-dev
pip install psycopg2
```
Configuración:
```
cp config.yml.template config.yml
```

En una consola psql:
```
create role checkeruser with login password '12345678';
create database checkertest with owner checkeruser;
```
