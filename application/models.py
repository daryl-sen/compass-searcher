from application import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime as dt

@login_manager.user_loader
def load_user(user_id):
  return Users.query.get(user_id)

class Users(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True, nullable = False)
  username = db.Column(db.String(100), index = True, nullable = False)
  password = db.Column(db.String(200), nullable = False)

  def __init__(self, username, password):
    self.username = username
    self.password = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.password, password)




class Pages(db.Model):
  id = db.Column(db.Integer, primary_key = True, nullable = False)
  ref_id = db.Column(db.String(10), index = True, nullable = False)
  heading = db.Column(db.String(150), index = True, nullable = False)
  activity_type = db.Column(db.String(50), index = True, nullable = False)
  instructions = db.Column(db.Text, index = True, nullable = False)
  duration = db.Column(db.String(50), nullable = False)
  link = db.Column(db.String(200), nullable = False)
  date_recorded = db.Column(db.DateTime, index = True, nullable = False)

  def __init__(self, ref_id, heading, activity_type, duration, instructions, link):
    self.ref_id = ref_id
    self.heading = heading
    self.activity_type = activity_type
    self.instructions = instructions
    self.duration = duration
    self.link = link
    self.date_recorded = dt.datetime.now()