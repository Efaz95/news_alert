# This file connects to the postgre data base using psycopg2
import os
import psycopg2

news_database_pass = os.environ.get("news_database_pass")

hostname = 'localhost'
username = 'efaz'
password = 'news_database_pass'
database = 'news_user_info'


conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
cur = conn.cursor()
cur.execute("SELECT email FROM signup_user")
#emails = all the emails stored in the database
emails = ([row[0] for row in cur.fetchall()])


conn.close()



