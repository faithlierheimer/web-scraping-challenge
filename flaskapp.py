#Import dependencies 
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template
from scrape_mars import init_browser, scrape
# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Define database and collection
db = client.mars_db
collection = db.mars

####Begin flask app routes######
@app.route("/")

@app.route("/scrape")
init_browser()
scrape()
