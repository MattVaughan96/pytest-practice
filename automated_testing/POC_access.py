import pytest
import requests
from artifactory import ArtifactoryPath


class PackageTest:

    def __init__(self):
        USERNAME = "Service_Account"
        PASSWORD = "password"
        # -cyberark generate password
        PATH = ArtifactoryPath("https://binarycentral.jfrog.io/artifactory/docker-hub/library", auth=(USERNAME, PASSWORD))

    def test_status(self):
        response = requests.get(self.PATH)
        assert response.status_code == 200

    def download_artefacts(self):
        with PATH.open() as fd, open("tomcat.tar.gz", "wb") as out:
            out.write(fd.read())



'''
if __name__ == '__main__'
    response = requests.get(path)
    assert response.status_code == 200
'''



x


# downloads artifact
with path.open() as fd, open("tomcat.tar.gz", "wb") as out:
    out.write(fd.read())


# test the artifact is downloaded
def test_package_download():
    response = requests.get(path)
    assert

    # potentially run something that searches what's installed 'list' and assert that 'artifact' is 'in' 'list'
    https: // stackoverflow.com / questions / 1051254 / check - if -python - package - is -installed

    # code to check installed successfully
