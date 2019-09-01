#!/usr/bin/python
import os
import psycopg2

news_database_pass = os.environ.get("news_database_pass")

hostname = 'localhost'
username = 'efaz'
password = 'news_database_pass'
database = 'news_user_info'




def doQuery( conn ) :
	cur = conn.cursor()
	cur.execute( "SELECT email FROM signup_user" )

	email_list = ([row[0] for row in cur.fetchall()])
	print(email_list)




myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()
