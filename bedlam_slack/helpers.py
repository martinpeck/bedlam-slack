import requests
import os

class SlackHelper():

  def __init__(self):
    
    self.token = os.environ.get("SLACK_TOKEN", "")
    self.team_name = os.environ.get("SLACK_TEAM", "")

  def validate_request(self):
    return True
    
  def extract_slash_command(self):
    return "cheese"