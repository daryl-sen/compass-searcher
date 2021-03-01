from function_modules import BASE_URL, login_to_compass, fetch_day_links, fetch_activity_links, fetch_activity_content, write_to_db


def run():
  BASE_URL = 'https://web.compass.lighthouselabs.ca'

  ses = login_to_compass()
  activity_links = fetch_day_links(ses, BASE_URL, '/days/today')

  for activity_link in activity_links:
    day_schedule = fetch_activity_links(ses, BASE_URL, activity_link)
    for schedule_item in day_schedule:
      day_content = fetch_activity_content(ses, BASE_URL, schedule_item)
      write_to_db(day_content)

if __name__ == "__main__":
  run()