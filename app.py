from flask import Flask, request
from routes import auth

app = Flask(__name__)

app.register_blueprint(auth.bp, url_prefix='/auth')

if __name__ == '__main__':
    #app.debug = True
    app.run()
