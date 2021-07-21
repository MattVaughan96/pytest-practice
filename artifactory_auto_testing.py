import pytest
import requests
import artifactory

def check_status_code_equals_200():
    url = "https://binarycentral.jfrog.io/artifactory/docker-hub/library"
    auth = HTTPBasicAuth(username,apiKey)
    response = requests.get(url,headers=headers,auth=auth,verify = "",proxies = proxyDict)
    assert response.status_code == 200

#mucking around
#more mucking
#even more mucking
