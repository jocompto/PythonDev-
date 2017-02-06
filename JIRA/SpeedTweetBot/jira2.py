# Test accessing JIRA from Python via REST API
# Documentation: http://jira.readthedocs.org/en/latest/# 
from jira import JIRA

options = {
    'server': 'https://jira.sset.jhu.edu/jira',
}
 
authed_jira = JIRA(server='https://jira.sset.jhu.edu/jira', basic_auth=('jcompto8', ''))

issue = jira.issue('SSC-3958')
print( issue.fields.project.key)             # 'SSC'
print( issue.fields.issuetype.name)          # 'Maintenance'
print( issue.fields.reporter.displayName)    # 'David DiGregorio'

# As of 2/4/2016 Not working - 
#<html><head>
#<title>404 Not Found</title>
#</head><body>
#<h1>Not Found</h1>
#Unauthorized (401)
#</body></html>