from jira import JIRA

jira = JIRA('https://jira.atlassian.com')

issue = jira.issue('JRA-9')
print( 'Project Key : ', issue.fields.project.key)             # 'JRA'
print( 'Issue Type  : ', issue.fields.issuetype.name)          # 'New Feature'
print( 'Reporter    : ',issue.fields.reporter.displayName)    # 'Mike Cannon-Brookes [Atlassian]'
print( 'Assignee    : ', issue.fields.assignee )
print( 'Description : ', issue.fields.description)

