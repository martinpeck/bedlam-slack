from nose.tools import *
import bedlam_slack
import json

class UD_Tests:

    def setup(self):
        self.app = bedlam_slack.app.test_client()

    def test_simple_word(self):
        response = self.app.post("/slash/urban-dictionary", data={'text': 'foo'})
        assert response.status_code == 200

        data = json.loads(response.get_data(as_text=True))

        assert data["text"] == "http://www.urbandictionary.com/define.php?term=foo"


    def test_leading_and_trailing_spaces(self):
        response = self.app.post("/slash/urban-dictionary", data={'text': '   foo   '})
        assert response.status_code == 200

        data = json.loads(response.get_data(as_text=True))

        assert data["text"] == "http://www.urbandictionary.com/define.php?term=foo"


    def test_spaces_in_phrase(self):
        response = self.app.post("/slash/urban-dictionary", data={'text': 'fish and chips'})
        assert response.status_code == 200

        data = json.loads(response.get_data(as_text=True))

        assert data["text"] == "http://www.urbandictionary.com/define.php?term=fish+and+chips"


    def test_amphersand_in_phrase(self):
        response = self.app.post("/slash/urban-dictionary", data={'text': 'Slap & Tickle'})
        assert response.status_code == 200

        data = json.loads(response.get_data(as_text=True))

        assert data["text"] == "http://www.urbandictionary.com/define.php?term=Slap+%26+Tickle"