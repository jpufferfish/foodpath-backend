
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
import os

# https://stackoverflow.com/a/42906465
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
cors = CORS(app)
# CORS(app, resources={r"/*": {"origins": "*"}})

# import declared routes
# even if they arent used/highlighted here, endpts wouldnt be found otherise
import users
import history
import recsys
import auth
import constants

@app.route("/hello")
@cross_origin()
def helloWorld():
  print("Hello, cross-origin-world!")
  return "Hello, cross-origin-world!"

# https://stackoverflow.com/a/65152383
# import ssl
# context = ssl.SSLContext()
# context.load_cert_chain('fullchain.pem', 'privkey.pem')

if __name__ == '__main__':
    app.run()
