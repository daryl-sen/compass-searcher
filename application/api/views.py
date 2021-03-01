from flask import render_template, Blueprint, request, jsonify, make_response
from application import db
from flask_login import login_user, login_required, logout_user, current_user

api = Blueprint('api', __name__, template_folder = 'templates/api')

@api.route('/', methods=['post', 'get'])
def index():
  return render_template('index.html')


@api.route('/search_results', methods=['get'])
@login_required
def search_results():
  pass