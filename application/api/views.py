from flask import render_template, Blueprint, request, jsonify, make_response
from application import db
from flask_login import login_user, login_required, logout_user, current_user
from application.models import Pages

api = Blueprint('api', __name__, template_folder = 'templates/api')

@api.route('/search', methods=['get'])
# @login_required
def index():
  query_term = 'emp'
  results = Pages.query.filter(Pages.instructions.contains(query_term)).all()
  return render_template('index.html')