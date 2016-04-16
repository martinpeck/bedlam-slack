from flask import Flask
app = Flask(__name__)

import bedlam_slack.random
import bedlam_slack.catgif
import bedlam_slack.testenv
import bedlam_slack.ud

@app.route("/")
def hello():
    return "Bedlam Slack Slash Commands"