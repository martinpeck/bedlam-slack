from flask import Flask
from flask import jsonify
from flask import request
from slack_helper import SlackHelper
import os

app = Flask(__name__)
slack_helper = SlackHelper()

@app.route("/")
def hello():
    return "Bedlam Slack Slash Commands"
    
# returns a random number. Well, sort of random.
@app.route("/slash/random-number", methods=['POST'])
def random():
    if not slack_helper.validate_request():
        abort(403)
    
    # chosen by fair dice roll, guaranteed to be random
    response = {
        "response_type": "in_channel",
        "text": "Your random number is: 4"
        }
        
    return jsonify(response)

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

# returns an UrbanDictionary URI
@app.route("/slash/urban-dictionary", methods=['POST'])
def urban_dictionary_uri():
    if not slack_helper.validate_request():
        abort(403)

    phrase = request.values.get('text').strip().replace(' ', '+')

    response = {
        "response_type": "in_channel",
        "text": "http://www.urbandictionary.com/define.php?term=" + phrase
    }

    return jsonify(response)
    
    
# for testing that environment variables are being picked up
@app.route("/test/env", methods=["GET"])
def test_environment():
    return os.environ["TEST_ENV_VALUE"]
     
if __name__ == "__main__":
    app.run(debug=True)
