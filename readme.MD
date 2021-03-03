# Compass Searcher

(Work in progress)

You've probably noticed that LHL compass doesn't have a search button. Perhaps it's an oversight, perhaps it's intentional. At the end of the day, it's just a huge inconvenience!

Imagine trying to find specific instructions from a previous day or previous week, checking the pages one by one like some archaic dinosaur. Well, that's going to change. Before we get started...

## Copyright Disclaimmer

Compass Searcher only provides a clickable link back to the target page and a short snippet (shorter than a tweet) to give context around the search term. It does not provide access to protected content (i.e. content that requires login).

## How Does It Work?
Compass Searcher has a page crawler component that logs in to compass and caches relevant parts of each page (using the calendar as an index). This information is stored inside an indexed databased which is refreshed in sync with course progress. When the user enters a search term, Compass Searcher searches the database and returns the pages that match the search term, providing a very short snippet around the search term for context.

## Stack
Compass Searcher uses React.js as the frontend, a SQLite database, and Python Flask as the backend framework. Why Flask instead of Express?
1. Flask comes with an ORM called SQLAlchemy, a tried-and-tested library that provides much better security. (Protecting LHL assets!)
2. Unlike Heroku, PythonAnywhere provides unrestricted uptime and online apps do not go to sleep due to inactivity. Since PythonAnywhere uses Python, the backend had to be written in Python instead oF JS. 


## Installation Instructions
You can use this online without any setup. The following is only needed if you want to run this app locally. Note that you need to supply your own Git username and password in the .env file. This is required for the crawler to login to Compass. All the code here is open source, nobody's going to steal your login information. More setup details to come.

### Dependencies
#### Python 3.5 or higher
* requests (crawler)
* beautifulsoup4 (crawler)
* lxml (crawler)
* python-dotenv
* flask
* flask-sqlalchemy
* flask-migrate
* flask-login
* flask-wtf
#### Node (React)
* Details to come

### Python Flask setup
1. Install dependencies - create a python virtual environment using `venv` or `virtualenv` and activate the environment.
2. Run `pip install -r requirements.txt` to automatically install python dependencies
3. Run `flask db init` to initialize the SQLite database
4. Run `flask db migrate` to migrate (setup) the database using the app's models
5. Run `flask db upgrade` to commit the initiation process.
6. Run `python app.py` to start a development server, then in a separate terminal, run `python scraper/test.py offline` to do an offline test. If you're not getting any errors or empty arrays, your flask app has been set up correctly!

### Setting up your github account
! Current as of March 2021 - this method may change in the future.
1. Make a copy of the `.env.example` file and rename it to `.env`.
2. Logout of github if you're currently logged in. Open the network tab of your developer console on the github login page, and then log back in to github.
3. In the network tab, the first item should be `session`. Right click on it and select `Copy` then `Copy as cURL`. Paste into any text editing software and look for the line starting with `  -H 'cookie:`. Copy everything starting from (not including) the first `:` to the last single quote `'` (not including the quote). Paste this value in the `.env` file, surrounded by single or double quotes. You should end up with `GIT_COOKIE='<your cookie here>'`,
4. Scroll down to `Form Data` and look for the `authenticity_token`, `login`, `password`, `timestamp`, and `timestamp_secret` keys. Copy these values into the corresponding keys in your `.env` file.
5. Once this is set up, run `python scraper/test.py online` in the root folder of this project directory. If you're not getting any errors or an empty array, the scraper has been set up correctly and is now ready to use. Run `python scraper/run.py` to start scraping and populating your database!

## Credits
Daryl Tang

