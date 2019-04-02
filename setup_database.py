#!/usr/bin/python3

import MySQLdb as mysql

databaseName = "redditcrawl"


# Create the database
# Connection to MySQL
createDB = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="")     # password

# Cursor to create first database
curCreateDB = createDB.cursor()

# Create database "redditcrawl"
curCreateDB.execute("CREATE DATABASE IF NOT EXISTS " + databaseName)
createDB.commit()


# Create the tables
# Connection to MySQL database
db = mysql.connect(host="localhost",
		   user="root",
		   passwd="",
	   database=databaseName
	   )

cur = db.cursor()

# create table "submission"
cur.execute("CREATE TABLE submission (
	id VARCHAR NOT NULL,
	subreddit VARCHAR NOT NULL,
	ups INT
	)"
	
db.commit()