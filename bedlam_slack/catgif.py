from bedlam_slack import app, slack_helper
from flask import jsonify
import requests
from bs4 import BeautifulSoup

CAT_API_URL = "http://thecatapi.com/api/images/get?format=xml&type=gif&results_per_page=1"
CAT_API_TOKEN = ""

# extract the url from the response text
def parse_cat_api_response(response_text):    
    soup = BeautifulSoup(response_text, "lxml")
    return soup.image.url.text

# returns a random cat gif from thecatapi.com
def get_cat_image(token, url):
    resp = requests.get(url)
    if resp.status_code == 200:       
        return parse_cat_api_response(resp.text)
        
@app.route("/slash/cat-gif", methods=['POST'])
def random_cat_gif():
    if not slack_helper.validate_request():
        abort(403)
    
    image_url = get_cat_image(CAT_API_TOKEN, CAT_API_URL)
     
    # return response
    response = {
        "response_type": "in_channel",
        "text": "Here is your random cat:",
        "attachments" : [
            {
                "fallback" : "A cat gif",
                "title" : "Random cat gif",
                "image_url" : image_url
            }
          ]
        }
        
    return jsonify(response)