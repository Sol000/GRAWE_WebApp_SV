# ------------------------------------------------------------------------
# Fileame:      routes.py
#
# Description:  Containes all routs/requests for this applicatin
#
# Authors:      TM, .....
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
#                              INCLUDES
# ------------------------------------------------------------------------
# libs
import json
from datetime import timezone, datetime, timedelta
from flask import request, jsonify
from flask_jwt_extended import create_access_token,get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required

# local
from server import app

# ------------------------------------------------------------------------
#                              ROUTES
# ------------------------------------------------------------------------
# <<<<<<<<<<<<<<<<<<<<<<<< Access-Handling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creates an session token
@app.route('/token', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    #TODO: Query DB with the request and check if USER and PASSWD are valid
    # This is only for testing
    if email != "test" or password != "test":
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response

# logout the user
@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

# extends lifespan of an token when its close to runout
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

# <<<<<<<<<<<<<<<<<<<<<<<< Application-Serving >>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/')
@jwt_required()
def main():
  #TODO: Program
  return "hallo"