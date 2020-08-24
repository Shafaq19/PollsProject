import psycopg2
import django
con = psycopg2.connect(database="polls", user="shafaq", password="ABC123ssi", host="127.0.0.1", port="5432")

print("Database opened successfully")