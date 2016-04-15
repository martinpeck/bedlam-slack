from flask import Flask
from flask import jsonify
from slack_helper import SlackHelper
import os

app = Flask(__name__)
slack_helper = SlackHelper()

@app.route("/")
def hello():
    return "Bedlam Slack Slash Commands"
    
@app.route("/slash/random-number", methods=['POST'])
def random():
    if not slack_helper.validate_request():
        abort(403)
    
    # chosen by fair dice roll
    # guarenteed to be random
    response = {
        "response_type": "in_channel",
        "text": "Your random number is: 4"
        }
        
    return jsonify(response)


@app.route("/slash/cat-gif", methods=['POST'])
def random_cat_gif():
    if not slack_helper.validate_request():
        abort(403)
    
    response = {
        "response_type": "in_channel",
        "text": "Here is your random cat:",
        "attachments" : [
            {
                "image-url" : "http://thecatapi.com/api/images/get?format=src&type=gif"
            }
          ]
        }
        
    return jsonify(response)

@app.route("/slash/echo", methods=['POST'])
def echo():
    return "hello"

@app.route("/test/env", methods=["GET"])
def test_environment():
    return os.environ["TEST_ENV_VALUE"]
     
if __name__ == "__main__":
    app.run(debug=True)
