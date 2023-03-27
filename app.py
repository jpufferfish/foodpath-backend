# from flask import Flask, request, abort
# from flask import Flask
# from users import users_app
# from logs import logs_app
# from threading import Thread
# import constants

# app = Flask(__name__)
# app.register_blueprint(users_app)
# app.register_blueprint(logs_app)

# if __name__ == '__main__':
#   app.run(host=constants.DEFAULT_HOST, port=constants.DEFAULT_PORT, debug=constants.DEFAULT_DEBUG)

# t = Thread(target=app.run)
# t.start()



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
    # print('starting')
    # context = ('local.crt', 'local.key')
    # app.run(host=constants.DEFAULT_HOST, port=constants.DEFAULT_PORT, debug=constants.DEFAULT_DEBUG)
    app.run()
    # app.run(ssl_context=context)
    # app.run(ssl_context='adhoc')