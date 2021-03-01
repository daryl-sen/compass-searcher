import sys
from function_modules import login_to_compass, fetch_day_links, fetch_activity_links, fetch_activity_content, BASE_URL, write_to_db

# test that runs on the actual LHL website
def production_test():
  BASE_URL = 'https://web.compass.lighthouselabs.ca'

  ses = login_to_compass()
  activity_links = fetch_day_links(ses, BASE_URL, '/days/today')
  print(activity_links)
  print('\n\n\n')

  # find day 1 schedule
  day_schedule = fetch_activity_links(ses, BASE_URL, activity_links[0])
  print(day_schedule)
  print('\n\n\n')

  # find day 1 activity 1
  day_content = fetch_activity_content(ses, BASE_URL, day_schedule[0])
  print(day_content)
  print('\n\n\n')

# test that runs on a fake LHL page setup on localhost
def offline_test():
  import requests
  from bs4 import BeautifulSoup


  BASE_URL = 'http://localhost:5000'
  ses = requests.Session()

  activity_links = fetch_day_links(ses, BASE_URL, '/offline_test/1')
  # print(activity_links)
  # print('\n\n\n')

  # find day 1 schedule
  day_schedule = fetch_activity_links(ses, BASE_URL, '/offline_test/2')
  # print(day_schedule)
  # print('\n\n\n')

  # find day 1 activity 1
  day_content = fetch_activity_content(ses, BASE_URL, '/offline_test/3')
  # print(day_content)
  # print('\n\n\n')

  write_to_db(day_content)


  





# which test to run

if len(sys.argv) > 1:
  mode = sys.argv[1]

  if mode == 'online':
    production_test()
  elif mode == 'offline':
    offline_test()
  else:
    print('Invalid mode entered. Please enter "online" or "offline" at the end of your python command. i.e. "python test.py offline"')

else:
  print('No mode entered. Please enter "online" or "offline" at the end of your python command. i.e. "python test.py offline"')