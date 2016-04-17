from nose.tools import *
import bedlam_slack

class Random_Tests:

    def setup(self):
        self.app = bedlam_slack.app.test_client()

    def test_random_response_code(self):
        response = self.app.post("/slash/random-number")
        assert response.status_code == 200
   
    def test_random_response_content(self):
        response = self.app.post("/slash/random-number")
        assert "Your random number is:" in response.data.decode('utf8')