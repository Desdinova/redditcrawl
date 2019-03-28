#!/usr/bin/python3

import MySQLdb as mysql

# Connection to MySQL
db = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="")     # password

# Cursor to execute queries
cur = db.cursor()

# create database "redditcrawl"
cur.execute("CREATE DATABASE IF NOT EXISTS redditcrawl")
db.commit()




