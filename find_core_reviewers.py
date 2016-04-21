# https://github.com/openstack/governance/blob/master/reference/projects.yaml
# Retreive the file above, the raw version of it.
# Need to parse the file above and figure out all of the projects. 
# Then go to Gerrit and figure out who the core reviewers are for each projects. 

import urllib2
targeturl = 'https://github.com/openstack/governance/blob/master/reference/projects.yaml'
print targeturl
filecontents = urllib2.urlopen(targeturl)

for line in filecontents:
	print line
