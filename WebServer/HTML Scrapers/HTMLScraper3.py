#!/usr/bin/python
 
import urllib.error
import urllib.request
from bs4 import BeautifulSoup

import getpass
from click.decorators import password_option
from pywin.dialogs.login import GetPassword

 
url = "https://collaborate.johnshopkins.edu/sites/SAP/SupportTeam/Dev/Shared%20Documents/QuickLinks/Shortcuts.htm" 
i_passwd = GetPassword('Password -')
# set up authentication info
# Needed to include realm - when none it failed to login
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='collaborate.johnshopkins.edu',
                       uri=r'https://collaborate.johnshopkins.edu/sites/SAP/SupportTeam/Dev/Shared%20Documents/QuickLinks/',
                       user='jcompto8',
                       passwd=i_passwd)
opener =  urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
try:
    res = opener.open( url)
    nodes = res.read()

    #html = urllib.request.urlopen(url).read()
    html = nodes
    soup=BeautifulSoup(html, "html.parser")
    
    # Retrieve a list of the anchor tags -- Note:  will not retrieve those inside a comment! 
    # Each tag is a like a dictionary of HTLM Attributes
    tags = soup('a')
    
    # get a list of anchor links and the accompanying text labels from a web page
    for tag in tags:    
        # myLabel = ' '.join(tag.get_text().split())
        print( tag.get('href', None),   ";",  ' '.join(tag.get_text().split())  )

except urllib.error.HTTPError as e:
    print('Login Failure')
    print(e.headers['www-authenticate'])
    