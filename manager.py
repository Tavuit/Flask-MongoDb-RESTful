# coding: utf-8
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from flask_wtf.csrf import CSRFProtect
from config import load_config
from flask_jwt_extended import JWTManager
from flask_cors import CORS

"""Create Flask app."""
app = Flask(__name__)

# Load config global
config = load_config()
app.config.from_object(config)

# Enable JWT
jwt = JWTManager(app)

#CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# CSRF protect
# CSRFProtect(app)

# Init db
db = MongoEngine()
db.init_app(app)

PORT = 8080

from application.controllers import *

if __name__ == '__main__':
    app.run(port=PORT)