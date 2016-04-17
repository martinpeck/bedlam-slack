from bedlam_slack import app, slack_helper
from flask import request, jsonify

# returns an UrbanDictionary URI
@app.route("/slash/urban-dictionary", methods=['POST'])
def urban_dictionary_uri():
    if not slack_helper.validate_request():
        abort(403)

    phrase = request.values.get("text").strip().replace(' ', '+')

    response = {
        "response_type": "in_channel",
        "text": "http://www.urbandictionary.com/define.php?term=" + phrase,
        "unfurl_links": "true"
    }
    
    return jsonify(response)
