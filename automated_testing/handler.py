import Pytest
import artifactory


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
