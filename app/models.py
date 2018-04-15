from . import db

class Images:
    def __init__(self,id,userImageURL,webformatURL):
        self.id= id
        self.userImageURL=userImageURL
        self.webformatURL=webformatURL
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitches.id'))
    def __repr__(self):
        return f'User {self.username}'
class Pitch(db.Model):
    __tablename__='pitches'
    id=db.Column(db.Integer,primary_key=True)
    category=db.Column(db.Integer,primary_key=True)
    def __repr__(self):
        return f'User {self.username}'
