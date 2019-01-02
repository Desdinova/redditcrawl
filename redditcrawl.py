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
	print("Title: " + post.title)
	print("ID: " + post.id)
	print("Score: " + str(post.score))
	print("Created: " + str(post.created))
	print(datetime.datetime.fromtimestamp(post.created).strftime("%Y-%m-%d %H:%M"))
	print("Created UTC: " + str(post.created_utc))
	print(datetime.datetime.utcfromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M"))
	print("URL: " + post.url)
	print("Upvote Ratio: " + str(post.upvote_ratio))
	print("Author: " + str(post.author))
	print("Author Fullname: " + str(post.author_fullname))
	print("Subreddit: " + str(post.subreddit))
	print("Subreddit-ID: " + str(post.subreddit_id))
	print("# of Comments: " + str(post.num_comments))
	print("Comments: " + str(post._comments_by_id))
	print("Text: " + str(post.selftext_html))
	print("\n")
