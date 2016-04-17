from flask import Flask
from bedlam_slack.helpers import SlackHelper

app = Flask(__name__)
slack_helper = SlackHelper()

import bedlam_slack.random
import bedlam_slack.catgif
import bedlam_slack.shakespeare
import bedlam_slack.ud
import bedlam_slack.diagnostic

@app.route("/")
def hello():
    return "Bedlam Slack Slash Commands"