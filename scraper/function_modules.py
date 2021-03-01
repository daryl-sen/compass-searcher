import requests
import os
from bs4 import BeautifulSoup
from request_info import headers, data # get the info required to login to github

# import the flask app db
import sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from application import db
from application.models import * 



BASE_URL = 'https://web.compass.lighthouselabs.ca'

# LOGIN TO COMPASS
def login_to_compass():
  session_obj = requests.Session()

  # login to github account and create session object to store cookies
  session_obj.post('https://github.com/session', headers=headers, data=data)

  # login to LHL compass using github account
  session_obj.get(BASE_URL + '/auth/github')

  return session_obj

# day links - links that link to specific day schedules
def fetch_day_links(s, BASE_URL, homepage_url):
  print('- Fetching day links from: ' + BASE_URL + homepage_url)
  # access the compass homepage, which contains links to all the pages
  request_homepage = s.get(BASE_URL + homepage_url)

  # analyze the homepage content to get day links
  content = BeautifulSoup(request_homepage.content, features='lxml')
  link_elements_container = content.find_all("td", class_="day unlocked")
  day_links = [ link.find('a').get('href') for link in link_elements_container]
  return day_links

# activity links - links in a day's schedule that link to a day's activities
def fetch_activity_links(s, BASE_URL, day_link):
  print('-- Fetching activity links from: ' + BASE_URL + day_link)
  request_day_schedule = s.get(BASE_URL + day_link)
  content = BeautifulSoup(request_day_schedule.content, features='lxml')
  activity_links_container = content.find_all("a", class_="activity")
  activity_links = [ link.get('href') for link in activity_links_container ]
  return activity_links

# activities - actual content of individual activities
def fetch_activity_content(s, BASE_URL, activity_link):
  print('--- Fetching activity from: ' + BASE_URL + activity_link)
  request_day_activities = s.get(BASE_URL + activity_link)
  content = BeautifulSoup(request_day_activities.content, features='lxml')
  
  # find instructions
  day_instructions = content.find('div', class_='instructions')

  # find metadata
  day_metadata = content.find_all("header", class_="splash")

  results = {
    'instructions': day_instructions,
    'metadata': day_metadata,
    'ref_id': activity_link.split('/')[2],
    'URL': BASE_URL + activity_link
  }
  return results

def write_to_db(day_content):
  page_heading = str(day_content['metadata'][0].find('h1').contents[0])

  # metadata reading is a little fragile because the splash header structure vary from page to page. Set to N/A, then set to actual data if no trouble encountered
  page_duration = 'N/A'
  page_type = 'N/A'

  if len(day_content['metadata']) != 0:
    if len(day_content['metadata'][0].find('small').contents) != 0:
      page_duration = str(day_content['metadata'][0].find('small').contents[0])
    if len(day_content['metadata'][0].contents) > 1:
      page_type = str(day_content['metadata'][0].contents[1])

  if day_content['instructions'] is not None:
    page_instructions = day_content['instructions'].get_text()
  else:
    page_instructions = 'Empty'
    
  page_ref_id = day_content['ref_id']
  page_link = day_content['URL']

  # write the extracted data into database
  new_page = Pages(page_ref_id, page_heading, page_type, page_duration, page_instructions, page_link)
  db.session.add(new_page)
  db.session.commit()