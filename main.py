from flask import Flask
from slack_helper import SlackHelper
import os

app = Flask(__name__)
validator = SlackValidator()

@app.route("/")
def hello():
    return "Bedlam Slack Slash Commands"
    
@app.route("/slash/random-number", methods=['POST'])
def random():
    if not slack_helper.is_request_valid:
        abort(403)
    
    # chosen by fair dice roll
    # guarenteed to be random
    return "Your random number is: 4"

@app.route("/slash/echo", methods=['POST'])    
def echo():
    return "hello"

@app.route("/test/env", methods=["GET"])
def test_environment():
    return os.environ["TEST_ENV_VALUE"]
     
if __name__ == "__main__":
    app.run(debug=True)
