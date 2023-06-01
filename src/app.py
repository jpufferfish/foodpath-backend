
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
import os

# https://stackoverflow.com/a/42906465
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
# cors = CORS(app)
# CORS(app, resources={r"/*": {"origins": "*"}})

# import declared routes
# even if they arent used/highlighted here, endpts wouldnt be found otherise
import users
import history
import recsys
import auth
import constants

# testing
# CORS 
@app.route("/hello")
# @cross_origin()
def helloWorld():
  print("Hello, cross-origin-world!")
  return "Hello, cross-origin-world!"

# https://stackoverflow.com/a/65152383
# import ssl
# context = ssl.SSLContext()
# context.load_cert_chain('fullchain.pem', 'privkey.pem')

# About localhost: 
# 1) I vaguely remember that there was an issue where a mobile simulator (rn expo)
# struggled to find this backend because of something to do with localhost and in-network ip addrs
# so when working with frontend, it might work with constants.SIMULATOR_IP_ADDRESS. 
# AFAIk localhost is easier to test/type out
# 2) https://stackoverflow.com/questions/33524826/localhost-not-working-in-chrome-127-0-0-1-does-work
# firefox is ok
if __name__ == '__main__':
  print('starting')
  app.run(host=constants.DEFAULT_HOST, port=constants.DEFAULT_PORT, debug=constants.DEFAULT_DEBUG)
    # app.run()
