#Import dependencies 
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from flask_pymongo import PyMongo
from splinter import Browser
from flask import Flask, render_template, redirect
from scrape_mars import init_browser, scrape
# # Initialize PyMongo to work with MongoDBs
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# # Define database and collection
# db = client.mars_db
# collection = db.mars

####Begin flask app routes######
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_data"
mongo = PyMongo(app)
@app.route("/")
def index():
    mars_data = mongo.db.mongo_mars_docs.find_one()
    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape")
#When I launch this one it launches scrape like 12 times before it actually does what I want
#I think the first issues is importing things into mongo--do i do that before the flask app? 
def scraper():
    #Run scrape fxn
    init_browser()
    mars_dict = mongo.db.mongo_mars_docs
    mars_info = scrape()
    return mars_info

if __name__ == "__main__":
    app.run(debug=True)
