#Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests
import pymongo 
from pymongo import MongoClient
import time

##Set up splinter to visit the URL for JPL featured space image 
def init_browser():
    executable_path = {'executable_path': r'C:\Program Files\Chromedriver\chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)
def scrape():
    browser = init_browser()
    #### Mars News Scraping Code
    # URL of page to be scraped
    nasa_news_url = 'https://mars.nasa.gov/news/'
    # Retrieve page with the requests module
    news_response = requests.get(nasa_news_url)
    # Create BeautifulSoup object; parse with 'lxml'
    news_soup = bs(news_response.text, 'lxml')
    #Find first headline to collect latest news title and paragraph text.
    headlines = news_soup.find_all('div', class_='content_title')
    latest_news_title = headlines[0].text
    latest_news_title = latest_news_title.strip()

    ##Find paragraph text of first article
    paragraph = news_soup.find_all('div', class_='image_and_description_container')
    #paragraph_latest_news = 
    first_article = paragraph[0]
    first_article_description = first_article.find('div', class_='rollover_description_inner')
    first_article_description = first_article_description.text.strip()
    first_article_description

    ##Scraping JPL for featured JPL image
    ##Set up splinter to visit the URL for JPL featured space image 
    executable_path = {'executable_path': r'C:\Program Files\Chromedriver\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    ##Set up URL to visit using chromedriver
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    #Click 'full image'
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    #Go to 'more info'
    browser.click_link_by_partial_text('more info')
    ##Find image URL of featured image 
    jpl_html = browser.html
    jpl_soup = bs(jpl_html, 'html.parser')
    featured_image_rel_path = jpl_soup.find('figure', class_='lede').a['href']

    ##append base url for JPL to featured image
    jpl_base_url = 'https://www.jpl.nasa.gov'

    ##Concatenate base_url and image url
    featured_image_full_url = jpl_base_url + featured_image_rel_path
    ####Scraping Mars Facts Webpage for tabular data####

    ##Set up URL to read with pandas
    facts_url = 'https://space-facts.com/mars/'

    ##Read tabular data from page w/pandas
    tables = pd.read_html(facts_url)

    ### Transpose table to make it usable
    mars_facts = tables[0]
    mars_facts_transposed = mars_facts.transpose()
    # print(mars_facts_transposed)

    ##Convert the data to an HTML table string
    mars_facts_transposed_html = mars_facts_transposed.to_html()
    # print(mars_facts_transposed_html)
    ##Export HTML table to its own file for later use
    html_table_file = open("table.html", "w")
    html_table_file.write(mars_facts_transposed_html)
    html_table_file.close()

    ####Scrape USGS for pictures of Mars Hemispheres###

    ####--Find Cerberus Image & Title

    ##Set up scraper for images of Mars' hemispheres, starting w/Cerberus
    # URL of page to be scraped
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

    # Retrieve page with the requests module
    cerberus_response = requests.get(cerberus_url)
    # Create BeautifulSoup object; parse with 'lxml'
    cerberus_soup = bs(cerberus_response.text, 'lxml')

    ##Find title for cerberus hemisphere image
    cerberus_title = cerberus_soup.find('title').text
    cerberus_title = cerberus_title.split('|')
    cerberus_title = cerberus_title[0]
    

    ##Find URL for cerberus hemisphere image
    cerberus_hemisphere = cerberus_soup.find_all('div', class_= 'wide-image-wrapper')
    cerberus_hemisphere = cerberus_hemisphere[0]
    cerberus_hemisphere = cerberus_hemisphere.find_all('img', class_='wide-image')
    cerberus_hemisphere = cerberus_hemisphere[0]
    cerberus_hemisphere = cerberus_hemisphere['src']

    ##Save base URL to save all urls to images 
    usgs_base_url = 'https://astrogeology.usgs.gov/'
    cerberus_full_url = usgs_base_url + cerberus_hemisphere
    

    #Initialize dictionary to save url image and title
    hemisphere_image_urls = [
        {"title": cerberus_title, "img_url": cerberus_full_url}
    ]


    ######--Find Valles Marineris Hemisphere Image & Title

    ##Set up scraper for images of Mars' hemispheres, now Valles Marineris
    # URL of page to be scraped
    valles_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    # Retrieve page with the requests module
    response = requests.get(valles_url)
    # Create BeautifulSoup object; parse with 'lxml'
    valles_soup = bs(response.text, 'lxml')

    ##Find title for Valles Marineris hemisphere image
    valles_title = valles_soup.find('title').text
    valles_title = valles_title.split('|')
    valles_title = valles_title[0]

    ##Find URL for valles hemisphere image
    valles_hemisphere = valles_soup.find_all('div', class_= 'wide-image-wrapper')
    valles_hemisphere = valles_hemisphere[0]
    valles_hemisphere = valles_hemisphere.find_all('img', class_='wide-image')
    valles_hemisphere = valles_hemisphere[0]
    valles_hemisphere = valles_hemisphere['src']
   

    ##Construct full image URL
    valles_full_url = usgs_base_url + valles_hemisphere
   

    ##Add to dictionary
    hemisphere_image_urls.append({"title": valles_title, "img_url": valles_full_url})
   


    #####---Find Schiaparelli Hemisphere Image & Title
    ##Set up scraper for images of Mars' hemispheres, now Schiaparelli
    # URL of page to be scraped
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

    # Retrieve page with the requests module
    schiaparelli_response = requests.get(schiaparelli_url)
    # Create BeautifulSoup object; parse with 'lxml'
    schiaparelli_soup = bs(schiaparelli_response.text, 'lxml')

    ##Find title for Schiaparelli Hemisphere image
    schiaparelli_title = schiaparelli_soup.find('title').text
    schiaparelli_title = schiaparelli_title.split('|')
    schiaparelli_title = schiaparelli_title[0]
    

    ##Find URL for schiaparelli hemisphere image
    schiaparelli_hemisphere = schiaparelli_soup.find_all('div', class_= 'wide-image-wrapper')
    schiaparelli_hemisphere = schiaparelli_hemisphere[0]
    schiaparelli_hemisphere = schiaparelli_hemisphere.find_all('img', class_='wide-image')
    schiaparelli_hemisphere = schiaparelli_hemisphere[0]
    schiaparelli_hemisphere = schiaparelli_hemisphere['src']

    ##Construct full image URL
    schiaparelli_full_url = usgs_base_url + schiaparelli_hemisphere

    ##Add to dictionary
    hemisphere_image_urls.append({"title": schiaparelli_title, "img_url": schiaparelli_full_url})

    #####---Find Syrtis Major Hemisphere Image & Title

    ##Set up scraper for images of Mars' hemispheres, now Syrtis Major
    # URL of page to be scraped
    syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

    # Retrieve page with the requests module
    syrtis_response = requests.get(syrtis_url)
    # Create BeautifulSoup object; parse with 'lxml'
    syrtis_soup = bs(syrtis_response.text, 'lxml')

    ##Find title for Syrtis Major Hemisphere image
    syrtis_title = syrtis_soup.find('title').text
    syrtis_title = syrtis_title.split('|')
    syrtis_title = syrtis_title[0]

    ##Find URL for Syrtis Major hemisphere image
    syrtis_hemisphere = syrtis_soup.find_all('div', class_= 'wide-image-wrapper')
    syrtis_hemisphere = syrtis_hemisphere[0]
    syrtis_hemisphere = syrtis_hemisphere.find_all('img', class_='wide-image')
    syrtis_hemisphere = syrtis_hemisphere[0]
    syrtis_hemisphere = syrtis_hemisphere['src']

    ##Construct full image URL
    syrtis_full_url = usgs_base_url + syrtis_hemisphere

    ##Add to dictionary
    hemisphere_image_urls.append({"title": syrtis_title, "img_url": syrtis_full_url})
    
    ##Put all info into final dictionary
    mars_info_dict = {
        "latest_news_title": latest_news_title,
        "latest_news_paragraph": first_article_description,
        "featured_image_url": featured_image_full_url,
        "mars_facts_table": str(mars_facts_transposed_html),
        "hemisphere_images": hemisphere_image_urls

    }
    #Load data into mongodb 
    mongo_mars_docs = []
    mongo_mars_docs += [mars_info_dict]
    cluster = MongoClient("mongodb://localhost:27107/mars_data")
    db = cluster['mars_data']
    collection = db['mars_data']
    collection.insert_many(mongo_mars_docs)
    return mars_info_dict
