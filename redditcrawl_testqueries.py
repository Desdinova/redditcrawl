#!/usr/bin/env python3

import praw, json

#
# Authentication
#
# open authdata.json and put contents in data-variable
with open("authdata.json") as f:
	data = json.load(f)

# from authdata.json
reddit = praw.Reddit(client_id=data["client_id"], client_secret=data["client_secret"], password=data["password"], user_agent=data["user_agent"], username=data["username"])

for submission in reddit.subreddit('sysadmin').comments(limit=10):
	print(submission.author)
	
for post in reddit.subreddit('sysadmin').hot(limit=10):
	print(post.title)
	
for comment in reddit.redditor('desdinovy').comments.new(limit=None):
	print("Comment: " + comment.fullname)
	
for subs in reddit.redditor('desdinovy').submissions.new(limit=None):
	print("Submission: " + subs.fullname)
