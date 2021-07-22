import pytest
import requests
import artifactory

def test_get_locations_for_us_90210_check_status_code_equals_200():
     response = requests.get("http://api.zippopotam.us/us/90210")
     assert response.status_code == 200

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
