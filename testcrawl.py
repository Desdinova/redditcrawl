#!/usr/bin/env python3

import praw
import json
import datetime

#
# Authentication
#
# open authdata.json and put contents in data-variable
with open("authdata.json") as f:
	data = json.load(f)

# from authdata.json
reddit = praw.Reddit(client_id=data["client_id"], client_secret=data["client_secret"], password=data["password"], user_agent=data["user_agent"], username=data["username"])


for post in reddit.subreddit('linuxadmin').new(limit=5):
	print(post)
	print("\n")
