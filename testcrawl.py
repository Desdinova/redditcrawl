#!/usr/bin/env python3

import praw
import json
import datetime
import MySQLdb as mysql

#
# Authentication
#
# open authdata.json and put contents in data-variable
with open("authdata.json") as f:
	data = json.load(f)

# from authdata.json
reddit = praw.Reddit(client_id=data["client_id"], client_secret=data["client_secret"], password=data["password"], user_agent=data["user_agent"], username=data["username"])


# connection to MySQL database
db = mysql.connect(host="localhost",
		   user="flno",
		   passwd="", db="redditcrawl")

cur = db.cursor()


# print attributes from submissions in linuxadmin
for post in reddit.subreddit('linuxadmin').new(limit=5):
	print(post.id)
	print(post.created)
	print(post.title)
	print("\n")
	# check if entry is present
	cur.execute("SELECT * FROM submission WHERE id='" + post.id + "'")