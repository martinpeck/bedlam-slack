from bedlam_slack import app
import os
from flask import jsonify, request

@app.route("/test/env", methods=["GET"])
def test_environment():
    return os.environ["TEST_ENV_VALUE"]
    
@app.route("/test/text-echo", methods=["POST"])
def echo_request_text_values():
    return request.values.get("text")
     