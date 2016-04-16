from bedlam_slack import app
from flask import jsonify
from bedlam_slack.helpers import SlackHelper

# returns a random cat gif from thecatapi.com
@app.route("/slash/cat-gif", methods=['POST'])
def random_cat_gif():
    if not slack_helper.validate_request():
        abort(403)
    
    response = {
        "response_type": "in_channel",
        "text": "Here is your random cat:",
        "attachments" : [
            {
                "fallback" : "A cat gif",
                "title" : "Random cat gif",
                "image_url" : "http://thecatapi.com/api/images/get?format=src&type=gif"
            }
          ]
        }
        
    return jsonify(response)