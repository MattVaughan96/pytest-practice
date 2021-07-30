import pytest
import requests
import artifactory

username = test_user
password = Pa55w0rd

path = artifactorypath(link, auth = (username, password))

def test_response():
  response = requests.get(path)
  assert response blah blah == 200
  

#code that asserts a package can be downloaded.
