from flask import Flask
from scrape import run as scrape_runner

app = Flask(__name__)

# http://localhost:8000/
@app.route("/", methods=['GET'])
def hello_world():
    # run other code here.
    return "Hello, world. this is Flask"

# http://localhost:8000/abc
@app.route("/abc", methods=['GET'])
def abc():
    # run other code here.
    return "Hello, world. this is abc"

@app.route("/box-office-mojo-scraper", methods=['POST'])
def box_office_scraper_view():
    # run other code here.
    scrape_runner()
    return {"data": [1,2,3]}