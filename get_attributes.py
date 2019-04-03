#!/usr/bin/env python3

import pprint, praw, json

# open authdata.json and put contents in data-variable
with open("authdata.json") as f:
	data = json.load(f)

# from authdata.json
reddit = praw.Reddit(client_id=data["client_id"], client_secret=data["client_secret"], password=data["password"], user_agent=data["user_agent"], username=data["username"])


print("=====commentAttrs=====")
print("\n")

# Attributes of "comment"
commentAttrs = reddit.comment(id='e6w0mfh')
print(commentAttrs.score) # to make it non-lazy
pprint.pprint(vars(commentAttrs))

print("\n")
print("=====redditorAttrs=====")
print("\n")

# Attributes of "redditor"
redditorAttrs = reddit.redditor(name='MinaEdwar')
print(redditorAttrs.created) # to make it non-lazy
pprint.pprint(vars(redditorAttrs))

print("\n")
print("=====submissionAttrs=====")
print("\n")

# Attributes of "Submission"
submissionAttrs = reddit.submission(id='6zub5c')
print(submissionAttrs.created) # to make it non-lazy
pprint.pprint(vars(submissionAttrs))
