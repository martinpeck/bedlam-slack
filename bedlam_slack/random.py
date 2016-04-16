from bedlam_slack import app, slack_helper
from flask import jsonify
    
# returns a random number. Well, sort of random.
@app.route("/slash/random-number", methods=['POST'])
def random():
    if not slack_helper.validate_request():
        abort(403)
    
    # chosen by fair dice roll, guarenteed to be random
    response = {
        "response_type": "in_channel",
        "text": "Your random number is: 4"
        }
        
    return jsonify(response)