from flask import Flask
app = Flask(__name__)

import bedlam_slack.random
import bedlam_slack.catgif
import bedlam_slack.testenv

@app.route("/")
def hello():
    return "Bedlam Slack Slash Commands"