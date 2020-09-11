#Import dependencies 
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from flask_pymongo import PyMongo
from splinter import Browser
from flask import Flask, render_template, redirect
import scrape_mars

####Begin flask app routes######
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    ## line 18 is creating the collection mars_data
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape")
##Somehow this is opening a bunch of browsers and breaking again. :() But it does work? like it scraped the new image, it just took forever?
def scraper():
    #Run scrape fxn
    # mars_dict = mongo.db.mongo_mars_docs

    mars_data = mongo.db.mars_data
    mars_stuff = scrape_mars.scrape()
    #line 27 is inserting the results of the scraper into my collection
    mars_data.update({}, mars_stuff, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
