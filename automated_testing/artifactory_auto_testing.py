import pytest
import requests
import artifactory

def func(x):
    return x+1

def test_answer():
    assert func(3) == 5

def check_status_code_equals_200():
    url = "https://binarycentral.jfrog.io/artifactory/docker-hub/library"
    auth = HTTPBasicAuth(username,apiKey)
    response = requests.get(url,headers=headers,auth=auth,verify = "",proxies = proxyDict)
    assert response.status_code == 200

def Check_package_download():
    url = "https://binarycentral.jfrog.io/artifactory/docker-hub/library"
    auth = HTTPBasicAuth(username,apiKey)
    response = requests.get(url,headers=headers,auth=auth,verify = "",proxies = proxyDict)

    #code that pip installs docker package
    
    #code to check installed successfully
<<<<<<< HEAD:automated_testing/artifactory_auto_testing.py

=======
>>>>>>> 106f70a13489a9e7d6a6c3c3f362560cc2d181b6:automated testing/artifactory_auto_testing.py
