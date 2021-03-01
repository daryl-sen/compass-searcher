import os
from dotenv import load_dotenv

load_dotenv()

# Git Login Data

## IMPORTANT!!
# Fill in the .env.example file with information from your git cookie. Refer to the documentation on github for where to find this information.

headers = {
    'authority': 'github.com',
    'cache-control': 'max-age=0',
    'origin': 'https://github.com',
    'upgrade-insecure-requests': '1',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://github.com/login',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'cookie': os.getenv('GIT_COOKIE'),
}

data = {
  'commit': 'Sign in',
  'authenticity_token': os.getenv('GIT_AUTHENTICITY_TOKEN'),
  'login': os.getenv('GIT_USERNAME'),
  'password': os.getenv('GIT_PASSWORD'),
  'trusted_device': '',
  'webauthn-support': 'supported',
  'webauthn-iuvpaa-support': 'unsupported',
  'return_to': '',
  'allow_signup': '',
  'client_id': '',
  'integration': '',
  'required_field_e2a2': '',
  'timestamp': os.getenv('GIT_TIMESTAMP'),
  'timestamp_secret': os.getenv('GIT_TIMESTAMP_SECRET')
}