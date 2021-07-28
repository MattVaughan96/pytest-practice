import pytest
import requests
from artifactory import ArtifactoryPath


USERNAME = "Service_Account"
PASSWORD = "password"
#-cyberark generate password 

path = ArtifactoryPath(
    "https://binarycentral.jfrog.io/artifactory/docker-hub/library",
    auth=(USERNAME, PASSWORD)
)



#test page has a reponse
def test_status_code_equals_200():
    response = requests.get(path)
    assert response.status_code == 200


#downloads artifact
with path.open() as fd, open("tomcat.tar.gz", "wb") as out:
    out.write(fd.read())
    
#test the artifact is downloaded
def test_package_download():
    response = requests.get(path)
    assert 

    #potentially run something that searches what's installed 'list' and assert that 'artifact' is 'in' 'list'
  https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed
    
    #code to check installed successfully

    
"""1. POC accessing repo - using dummy account - 2
2. security - access password though cyberark - create safe - dynamic generate password - 5
3. on prem services can connect to artifactory and the repo isn't cached - accessing most up to date version -3
4. Publishes results to tools like Jira/Confluence page - 3
5. Make extendable so that other package types -3
"""
