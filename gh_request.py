# Making simple requests to the github API

import requests
import operator

#####################################################################
# get_contributors: Requests the contributors for a given github repo
#
# Parameters:
# - repo: name of github repo
# - owner: username of repo owner 
#
# Returns:
# - json object containing information about the contributors
#####################################################################
def get_contributors(repo, owner):
    gh_repos_url = 'https://api.github.com/repos/'
    contributors_api = '/stats/contributors'
    request_url = gh_repos_url + owner + '/' + repo + contributors_api

    print 'Getting Contributors...'
    response = requests.get(request_url)
    response.raise_for_status()

    return response.json()

#####################################################################
# get_contributor_details: 
# - Extracts the username and number of commits for each contributor
#
# Parameters:
# - contributors_json: json object response from github API
#
# Returns:
# - a list of (contributor, commits) reverse-sorted by commits
#####################################################################
def get_contributor_details(contributors_json):
    contributors = {}
    for i in xrange(len(contributors_json)):
        contributor = contributors_json[i]['author']['login']
        commits = contributors_json[i]['total']
        contributors[contributor] = commits

    return sorted(contributors.items(), key=operator.itemgetter(1),
        reverse=True)

#####################################################################
# get_top_ten_contributors: 
# - Get a list of the top 10 contributors to a particular github repo
#
# Parameters:
# - Entered by user: github repo name and owner
#
# Returns:
# - a list of the names of the top 10 contributors and their commit 
#   count
#####################################################################
def get_top_ten_contributors():
    repo = raw_input('Repo Name: ')
    owner = raw_input('Repo Owner: ')

    contributors_json = get_contributors(repo, owner)
    contributors = get_contributor_details(contributors_json)
    print contributors

    for i in xrange(0, min(10, len(contributors))):
        print str(i+1) + ") User: %s\n   Commits: %d" % contributors[i]

