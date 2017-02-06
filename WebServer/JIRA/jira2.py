# Test accessing JIRA from Python via REST API
# Documentation: http://jira.readthedocs.org/en/latest/# 
from jira import JIRA
import getpass
from click.decorators import password_option
from pywin.dialogs.login import GetPassword

options = {
    'server': 'https://jiratest.sset.jhu.edu/jira/secure',
    'server':'https://jiratest.sset.jhu.edu/jira/rest/api/2/',
    'server': 'https://jira.sset.jhu.edu/jira',
}
#https://jiratest.sset.jhu.edu/jira/rest/api/2/search?jql=project=SSC+AND+status=Open+order+by+duedate&fields=id,key 
#password_option = '*' 

passwd = GetPassword('Password -')

#authed_jira = JIRA(basic_auth=('jcompto8',passwd) )

jira = JIRA(server='https://jiratest.sset.jhu.edu/jira/secure', basic_auth=('jcompto8', passwd)  )

 

issue = jira.issue('SSC-3826')
print( issue.fields.project.key)             # 'SSC'
print( issue.fields.issuetype.name)          # 'Maintenance'
print( issue.fields.reporter.displayName)    # 'David DiGregorio'
print (issue.fields.customfield_10062 )

#for anames in  issue.fields.cf[10062] : 
#    print ('Participants: ', anames.assignee.displayName )
#issue.fields.customfield_10062
# As of 2/4/2016 Not working - 
#<html><head>
#<title>404 Not Found</title>
#</head><body>
#<h1>Not Found</h1>
#Unauthorized (401)
#</body></html>
#--------------------------------------------------------------- 
#List all issues for a project
# block_size = 100
# block_num = 0
# while True:
#     start_idx = block_num*block_size
#     issues = jira.search_issues(jql, start_idx, block_size)
#     if len(issues) == 0:
#         # Retrieve issues until there are no more to come
#         break
#     block_num += 1
#     for issue in issues:
#         log.info('%s: %s' % (issue.key, issue.fields.summary))