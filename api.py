import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_restful import Api
from controllers import user_controller
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

app = Flask(__name__)

api = Api(app)


api.add_resource(user_controller.UserController, "/api/user")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
