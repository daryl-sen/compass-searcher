import sys
from function_modules import login_to_compass, fetch_day_links, fetch_activity_links, fetch_activity_content, BASE_URL, write_to_db

# test that runs on the actual LHL website
def online_test():
  BASE_URL = 'https://web.compass.lighthouselabs.ca'

  ses = login_to_compass()
  activity_links = fetch_day_links(ses, BASE_URL, '/days/today')
  if len(activity_links) != 0:
    print('Login successful')
  else:
    print('Login failed')
    return 

  # find day 1 schedule
  day_schedule = fetch_activity_links(ses, BASE_URL, activity_links[0])
  if len(day_schedule) != 0:
    print('Fetched day schedule')
  else:
    print('Error fetching day schedule')
    return

  # find day 1 activity 1
  day_content = fetch_activity_content(ses, BASE_URL, day_schedule[0])
  if len(day_content) != 0:
    print('Fetched day content')
  else:
    print('Error fetching day content')
    return

# test that runs on a fake LHL page setup on localhost
def offline_test():
  import requests
  from bs4 import BeautifulSoup


  BASE_URL = 'http://localhost:9000'
  ses = requests.Session()

  activity_links = fetch_day_links(ses, BASE_URL, '/offline_test/1')
  if len(activity_links) != 0:
    print('Successfully fetched activity links')
    print(activity_links)
  else:
    print('Fetching activity links failed')
    return

  # find day 1 schedule
  day_schedule = fetch_activity_links(ses, BASE_URL, '/offline_test/2')
  if len(day_schedule) != 0:
    print('Fetched day schedule')
  else:
    print('Error fetching day schedule')
    return

  # find day 1 activity 1
  day_content = fetch_activity_content(ses, BASE_URL, '/offline_test/3')
  if len(day_content) != 0:
    print('Fetched day content')
  else:
    print('Error fetching day content')  
    return





# which test to run

if len(sys.argv) > 1:
  mode = sys.argv[1]

  if mode == 'online':
    online_test()
  elif mode == 'offline':
    offline_test()
  else:
    print('Invalid mode entered. Please enter "online" or "offline" at the end of your python command. i.e. "python test.py offline"')

else:
  print('No mode entered. Please enter "online" or "offline" at the end of your python command. i.e. "python test.py offline"')