import pytest
import requests
from artifactory import ArtifactoryPath

USERNAME = "name"
PASSWORD = "password"


path = ArtifactoryPath(
    "https://binarycentral.jfrog.io/artifactory/docker-hub/library",
    auth=(USERNAME, PASSWORD),
)
#downloads artifact
with path.open() as fd, open("tomcat.tar.gz", "wb") as out:
    out.write(fd.read())

def test_status_code_equals_200():
    response = requests.get(path)
    assert response.status_code == 200

def test_package_download():
    response = requests.get(path)
    assert 

  
    
    #code to check installed successfully
