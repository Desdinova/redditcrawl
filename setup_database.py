#!/usr/bin/python3

import MySQLdb as mysql

databaseName = "redditcrawl"


# create the database
# connection to MySQL
createDB = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="")     # password

# cursor to create first database
curCreateDB = createDB.cursor()

# create database
curCreateDB.execute("CREATE DATABASE IF NOT EXISTS " + databaseName + " CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
createDB.commit()


# create the tables
# connection to MySQL database
db = mysql.connect(host="localhost",
		   user="root",
		   passwd="", db=databaseName)

cur = db.cursor()

# create table "submission"
cur.execute("CREATE TABLE submission (id VARCHAR (191) NOT NULL UNIQUE, ups INT, _fetched BIT, _flair CHAR, _mod CHAR, approved_at_utc DATETIME, approved_by TINYTEXT, archived BIT, author TINYTEXT, author_fullname TINYTEXT, banned_at_utc DATETIME, banned_by TINYTEXT, clicked BIT, comment_limit SMALLINT, contest_mode BIT, created DATETIME, created_utc DATETIME, domain TEXT, downs MEDIUMINT, edited BIT, gilded SMALLINT, gildings CHAR, is_crosspostable BIT, is_meta BIT, is_original_content BIT, is_reddit_media_domain BIT, is_self BIT, is_video BIT, likes BIT, locked BIT, media TEXT, media_only BIT, name TINYTEXT, no_follow BIT, num_comments SMALLINT, num_crossposts TINYINT, num_reports TINYINT, over_18 BIT, permalink TEXT, pinned BIT, pwls MEDIUMINT, removal_reason TEXT, report_reasons TEXT, score MEDIUMINT, selftext LONGTEXT, selftext_html LONGTEXT, spoiler BIT, stickied BIT, subreddit TEXT, subreddit_id TINYTEXT, subreddit_name_prefixed TEXT, subreddit_subscribers MEDIUMINT, subreddit_type TINYTEXT, title TEXT, upvote_ratio FLOAT, url TEXT, view_count MEDIUMINT, wls SMALLINT)")
db.commit()

# create table "redditor"
cur.execute("CREATE TABLE reddior (fetched BIT, _path TEXT, _stream TEXT, comment_karma INT, created DATETIME, created_utc DATETIME, has_subscribed BIT, has_verfied_email BIT, icon_img TEXT, id VARCHAR(191) NOT NULL UNIQUE, is_employee BIT, is_friend BIT, is_gold BIT, is_mod BIT, link_karma INT, verified BIT")