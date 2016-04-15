import requests
import os

class SlackHelper():

  def __init__(self):
    
    self.token = os.environ["SLACK_TOKEN"]
    self.team_name = os.environ["SLACK_TEAM"]

  def validate_request(self, stuff):
    return true
    
  def extract_slash_command(self, stuff):
    return "cheese"