from flask import render_template, Blueprint, request
from application import db
from flask_login import login_user, login_required, logout_user, current_user
from application.models import Pages

mpa = Blueprint('mpa', __name__, template_folder = 'templates/mpa')

@mpa.route('/search', methods=['get'])
# # @login_required
def search():
  if request.args.get('term'):
    query_term = request.args.get('term')
  else:
    return render_template('mpa_search.html', results = 'undefined')

  results = Pages.query.filter(Pages.instructions.contains(query_term)).all()

  def process_instructions(raw):
    searchable_raw = raw.lower()
    target_start_loc = searchable_raw.find(query_term.lower())
    target_end_loc = target_start_loc + len(query_term)
    target_before = raw[target_start_loc - 50: target_start_loc]
    target_after = raw[target_end_loc: target_end_loc + 50]
    target = raw[target_start_loc:target_end_loc]

    return {
      'before': '... ' + target_before,
      'after': target_after + ' ...'
    }

  processed_results = [
    {
      'ref_id': result.ref_id,
      'heading': result.heading,
      'type': result.activity_type,
      'duration': result.duration,
      'URL': result.link,
      'date': result.date_recorded,
      'context_before': process_instructions(result.instructions)['before'],
      'context_after': process_instructions(result.instructions)['after'],
      'query_term': f"<span class='highlighted'>{query_term}</span>",
    } for result in results
  ]

  return render_template('mpa_search.html', results = processed_results)