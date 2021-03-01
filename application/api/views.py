from flask import render_template, Blueprint, request, jsonify, make_response
from application import db
from flask_login import login_user, login_required, logout_user, current_user
from application.models import Pages

api = Blueprint('api', __name__, template_folder = 'templates/api')

@api.route('/search', methods=['get'])
# @login_required
def index():
  query_term = 'stack'
  results = Pages.query.filter(Pages.instructions.contains(query_term)).all()

  def process_instructions(raw):
    searchable_raw = raw.lower()
    target_start_loc = searchable_raw.find(query_term.lower())
    target_end_loc = target_start_loc + len(query_term)
    target_before = raw[target_start_loc - 50: target_start_loc]
    target_after = raw[target_end_loc: target_end_loc + 50]

    return '...' + target_before + f"<span>{query_term}</span>" + target_after + '...'

  processed_results = [
    {
      'ref_id': result.ref_id,
      'heading': result.heading,
      'type': result.activity_type,
      'context': process_instructions(result.instructions),
      'duration': result.duration,
      'URL': result.link,
      'date': result.date_recorded
    } for result in results
  ]

  for result in processed_results:
    print(result['context'])
  return render_template('index.html')


@api.route('/mpa_search', methods=['get'])
# @login_required
def mpa_search():
  if request.args.get('term'):
    query_term = request.args.get('term')
  else:
    return render_template('mpa_search.html', results = 'None')

  results = Pages.query.filter(Pages.instructions.contains(query_term)).all()

  def process_instructions(raw):
    searchable_raw = raw.lower()
    target_start_loc = searchable_raw.find(query_term.lower())
    target_end_loc = target_start_loc + len(query_term)
    target_before = raw[target_start_loc - 50: target_start_loc]
    target_after = raw[target_end_loc: target_end_loc + 50]
    target = raw[target_start_loc:target_end_loc]

    return '...' + target_before + f"<span>{target}</span>" + target_after + '...'

  processed_results = [
    {
      'ref_id': result.ref_id,
      'heading': result.heading,
      'type': result.activity_type,
      'context': process_instructions(result.instructions),
      'duration': result.duration,
      'URL': result.link,
      'date': result.date_recorded
    } for result in results
  ]

  return render_template('mpa_search.html', results = processed_results)