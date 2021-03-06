from flask_restful import Resource
from flask import request
from db_setup import db
from models import User


class UserController(Resource):
    def get(self):
        users = User.query.all()
        return {"Users": [i.json() for i in users]}

    def post(self):
        data = request.json
        username = data.get("username")
        user = User(username)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            return {"response": "e"}
        return {"response": user.json()}
