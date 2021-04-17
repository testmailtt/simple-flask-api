from db_setup import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User %r>" % self.username

    def json(self):
        return {"username": self.username}


# if __name__ == "__main__":
#     db.create_all()
#     db.session.commit()