#!/usr/bin/python3

import MySQLdb as mysql

databaseName = "redditcrawl"

# Connection to MySQL
createDB = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="")     # password

# Cursor to create first database
cur = createDB.cursor()

# create database "redditcrawl"
cur.execute("CREATE DATABASE IF NOT EXISTS " + databaseName)
db.commit()





