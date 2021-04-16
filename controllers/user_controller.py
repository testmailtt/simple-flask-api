from flask_restful import Resource


class UserController(Resource):
    def get(self):
        return {"response": "User"}

    def post(self):
        return {"response": "User created"}
