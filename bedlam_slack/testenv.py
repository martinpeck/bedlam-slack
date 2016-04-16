from bedlam_slack import app
import os

# for testing that environment variables are being picked up
@app.route("/test/env", methods=["GET"])
def test_environment():
    return os.environ["TEST_ENV_VALUE"]
     