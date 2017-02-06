#!/usr/bin/python
 

import urllib.request
from bs4 import BeautifulSoup

# url = input('Enter URL -')
# url =  "http://skimfeed.com/"
url = "file:///C:/Users/jcompto8/Documents/GitHub/JHU-Shortcuts/Shortcuts.htm"
# url = "https://collaborate.johnshopkins.edu/sites/SAP/SupportTeam/Dev/Shared%20Documents/QuickLinks/Shortcuts.htm"
 
html = urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, "html.parser")

# Retrieve a list of the anchor tags -- Note:  will not retrieve those inside a comment! 
# Each tag is a like a dictionary of HTLM Attributes
tags = soup('a')

# get a list of anchor links and the accompanying text labels from a web page
for tag in tags:    
    # myLabel = ' '.join(tag.get_text().split())
    print( tag.get('href', None),   ";",  ' '.join(tag.get_text().split())  )

