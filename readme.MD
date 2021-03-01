# Compass Searcher

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
You can run this application locally if you like, but you need to supply your own Git username and password. This is required for the crawler to login to Compass. All the code here is open source, nobody's going to steal your login information. More setup details to come.

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

## Credits
Daryl Tang

