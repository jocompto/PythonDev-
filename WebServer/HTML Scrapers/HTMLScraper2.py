#!/usr/bin/python
import mechanicalsoup
import argparse

import urllib.request
from bs4 import BeautifulSoup

# url = input('Enter URL -')
url =  "http://skimfeed.com/"
url2 = "https://login.johnshopkins.edu/cgi-bin/allinonelogin.pl?BASIC=FALSE&AUTHDB=PROD&AUTHLEVEL=RISK&RD=20120821&TIMESTRING=1465332609"
url = "https://collaborate.johnshopkins.edu/sites/SAP/SupportTeam/Dev/Shared%20Documents/QuickLinks/Shortcuts.htm"

parser = argparse.ArgumentParser(description='Login to GitHub.')
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()
# change

browser = mechanicalsoup.Browser()
# request github login page. the result is a requests.Response object http://docs.python-requests.org/en/latest/user/quickstart/#response-content
login_page = browser.get("https://github.com/login")

# login_page.soup is a BeautifulSoup object http://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup 
# we grab the login form
login_form = login_page.soup.select("#login")[0].select("form")[0]

# specify username and password
login_form.select("#login_field")[0]['value'] = args.username
login_form.select("#password")[0]['value'] = args.password

# (or alternatively)
# login_form.input({"login": args.username, "password": args.password})

# submit form
page2 = browser.submit(login_form, login_page.url)

# verify we are now logged in
messages = page2.soup.find('div', class_='flash-messages')
if messages:
    print(messages.text)
assert page2.soup.select(".logout-form")

print(page2.soup.title.text)

# verify we remain logged in (thanks to cookies) as we browse the rest of the site
page3 = browser.get("https://github.com/hickford/MechanicalSoup")
assert page3.soup.select(".logout-form")

# html = urllib.request.urlopen(url).read()
# soup=BeautifulSoup(html, "html.parser")
# 
# # Retrieve a list of the anchor tags -- Note:  will not retrieve those inside a comment! 
# # Each tag is a like a dictionary of HTLM Attributes
# tags = soup('a')
# 
# for tag in tags:
# 
#     print( tag.get('href', None))

