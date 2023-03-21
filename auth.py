
# https://dev.to/nagatodev/how-to-add-login-authentication-to-a-flask-and-react-application-23i7
import json
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager

from users import CORS, get_user_by_username
from __main__ import app
CORS(app, resources={r"/*": {"origins": "*"}})

# https://www.grc.com/passwords.htm
app.config["JWT_SECRET_KEY"] = "F44DC3A9A5E5D58BBB448A06A1158D7535AA6452C989274B7A7BB6743D226ECC"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

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

@app.route('/token', methods=["POST"])
def create_token():
    print('request.json:'+str(request.json))
    username = request.json.get("username", None)
    user = get_user_by_username(username)
    print('user:'+str(user))
    password = request.json.get("password", None)
    if username != user['username'] or password != user['password']:
        return {"msg": "Wrong email or password"}, 401
    access_token = create_access_token(identity=username)
    response = {"access_token":access_token}
    return response

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@app.route('/profile')
@jwt_required()
def my_profile():
    print('profile')
    response_body = {
    }
    return response_body

