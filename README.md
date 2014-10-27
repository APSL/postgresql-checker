postgresql-checker
==================

Dependencias: 
pip instal psycopg2

Configuración:
cp config.yml.template config.yml

En psql:
create role checkeruser with login password '12345678';
create database checkertest with owner checkeruser;
