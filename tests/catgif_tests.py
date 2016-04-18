from nose.tools import *
import bedlam_slack
import json
import responses

class CatGit_Tests:
            
    def setup(self):
        self.app = bedlam_slack.app.test_client()
        self.response_text = """<?xml version="1.0"?>
            <response>
            <data>
                <images>
                <image>
                    <url>http://foo.bar.baz/123/456</url>
                    <id>test</id>
                    <source_url>http://thecatapi.com/?id=test</source_url>
                </image>
                </images>
            </data>
            </response>
        """

    def test_parse_cat_api_response(self):
    
        resp = bedlam_slack.catgif.parse_cat_api_response(self.response_text)
        assert resp["image_url"] == "http://foo.bar.baz/123/456"  
        assert resp["title_url"] == "http://thecatapi.com/?id=test"       
   
    @responses.activate
    def test_cat_gif_requests_are_working(self):
    
        # set up mock response from API
        responses.add(responses.GET, "http://thecatapi.com/api/images/get",
              body=self.response_text, status=200,
              content_type='application/json')

        # act      
        response = self.app.post("/slash/cat-gif")

        # assert    
        assert response.status_code == 200       
        data = json.loads(response.get_data(as_text=True))

        assert data.get("text") is not None
        assert data["text"] ==  "Here is your random cat:"
        
        assert data.get("attachments") is not None
        assert len(data["attachments"]) == 1
        
        attachment = data["attachments"][0]
        
        assert attachment.get("image_url") is not None
        assert attachment["image_url"] == "http://foo.bar.baz/123/456"
        
        assert attachment.get("title_link") is not None
        assert attachment["title_link"] == "http://thecatapi.com/?id=test"