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



# print('starting')
    # context = ('local.crt', 'local.key')
    # app.run(host=constants.DEFAULT_HOST, port=constants.DEFAULT_PORT, debug=constants.DEFAULT_DEBUG)
    # app.run(ssl_context=context)
    # app.run(ssl_context='adhoc')