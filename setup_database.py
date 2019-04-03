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
curCreateDB.execute("CREATE DATABASE IF NOT EXISTS " + databaseName + " CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
createDB.commit()


# Create the tables
# Connection to MySQL database
db = mysql.connect(host="localhost",
		   user="root",
		   passwd="", db=databaseName)

cur = db.cursor()

# create table "submission"
cur.execute("CREATE TABLE submission (id VARCHAR (191) NOT NULL UNIQUE, subreddit VARCHAR (255) NOT NULL, ups INT, _fetched BIT, _flair CHAR, _mod CHAR, approved_at_utc TIMESTAMP)")

db.commit()