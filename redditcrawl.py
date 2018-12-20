#!/usr/bin/env python

import praw, json

#
# Authentication
#
# open authdata.json and put contents in data-variable
with open("authdata.json") as f:
	data = json.load(f)

# from authdata.json
reddit = praw.Reddit(client_id=data["client_id"], client_secret=data["client_secret"], password=data["password"], user_agent=data["user_agent"], username=data["username"])

for submission in reddit.front.hot(limit=256):
	print(submission.score)
