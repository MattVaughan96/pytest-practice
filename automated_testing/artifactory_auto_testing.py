import pytest
import requests
from artifactory import ArtifactoryPath
from dohq_artifactory import generate_password, User

USERNAME = "name"
PASSWORD = "password"


    
#find user
user = artifactory_.find_user("username")
#creates new user
if user is None:
    # User does not exist
    user = User(
        artifactory_, "username", "username@bankofengland.co.uk", password=generate_password()
    )
    user.create()

path = ArtifactoryPath(
    "https://binarycentral.jfrog.io/artifactory/docker-hub/library",
    auth=(USERNAME, PASSWORD) #user.username, user.password
)
#downloads artifact
with path.open() as fd, open("tomcat.tar.gz", "wb") as out:
    out.write(fd.read())

#test page has a reponse
def test_status_code_equals_200():
    response = requests.get(path)
    assert response.status_code == 200

#test the artifact is downloaded
def test_package_download():
    response = requests.get(path)
    assert 

    #potentially run something that searches what's installed 'list' and assert that 'artifact' is 'in' 'list'
  https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed
    
    #code to check installed successfully
