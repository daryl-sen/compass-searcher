from flask import render_template, Blueprint, redirect, url_for, flash, request, jsonify, make_response
from application.forms import login_form
from application.models import Users
from application import db
from flask_login import login_user, login_required, logout_user, current_user

core = Blueprint('core', __name__, template_folder = 'templates/core')

@core.route('/', methods=['post', 'get'])
def index():
  return render_template('index.html')

@core.route('/login', methods=['post', 'get'])
def login():
  form = login_form()
  if form.validate_on_submit():
    this_user = Users.query.filter_by(username = form.username.data.lower()).first()
    if this_user is not None and this_user.check_password(form.password.data):
      login_user(this_user)
      flash(f'Welcome back, {this_user.username}')      
      next = request.args.get('next')
      if next == None or not next[0]=='/':
        next = url_for('core.index')
      return redirect(next)
    else:
      flash('You have provided a wrong email or password.')
      return redirect(url_for('core.login'))
  else:
    for field, error in form.errors.items():
      flash('{} ({} error)'.format(error[0], field))
  return render_template('login.html', form = form)

@core.route('/logout')
@login_required
def logout():
  logout_user()
  flash('Logged out.')
  return redirect(url_for('core.login'))

# The following route is for offline scraper testing only. Remove during production
@core.route('/offline_test/<int:phase>')
def test(phase):
  if phase == 1:
    return render_template('phase1.html')
  elif phase == 2:
    return render_template('phase2.html')
  elif phase == 3:
    return render_template('phase3.html')