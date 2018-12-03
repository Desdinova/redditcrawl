#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/learnprogramming/comments/a1rp7c/i_made_a_python_web_scraping_guide_for_beginners/'

r = requests.get(url)

print(r.content)
