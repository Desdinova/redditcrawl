# redditcrawl

Preparatory work:

	sudo apt install python3-pip
	pip3 install praw
	sudo apt install mariadb-server
	sudo apt install python3-mysqldb
	sudo ./setup_database.py
	
(Optional) Grant access to database for other user than root

	sudo myql
	CREATE USER new_user@localhost;
	GRANT ALL PRIVILEGES ON redditcrawl.* to new_user@localhost;
