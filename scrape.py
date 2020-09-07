
#Import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser

####SCRAPING CODE#######
##Scraping NASA for most recent news story###
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
print(latest_news_title)

##Find paragraph text of first article
paragraph = news_soup.find_all('div', class_='image_and_description_container')
#paragraph_latest_news = 
first_article = paragraph[0]
first_article_description = first_article.find('div', class_='rollover_description_inner')
first_article_description = first_article_description.text.strip()
print(first_article_description)

##### Scraping JPL for featured space image #####

##Set up splinter to visit the URL for JPL featured space image 
executable_path = {'executable_path': r'C:\Program Files\Chromedriver\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

##Set up URL to visit using chromedriver
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)

##Find image URL of featured image 
jpl_html = browser.html
jpl_soup = bs(jpl_html, 'html.parser')
featured_image_rel_path = jpl_soup.find_all('img')[3]["src"]
print(featured_image_rel_path)

##append base url for JPL to featured image
jpl_base_url = 'https://www.jpl.nasa.gov'

##Concatenate base_url and image url
featured_image_full_url = jpl_base_url + featured_image_rel_path
print(featured_image_full_url)

####Scraping Mars Facts Webpage for tabular data####

# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

# In[48]:


##Set up URL to read with pandas
url = 'https://space-facts.com/mars/'


# In[51]:


##Read tabular data from page w/pandas
tables = pd.read_html(url)
tables[0]


# In[54]:


mars_facts = tables[0]
mars_facts_transposed = mars_facts.transpose()
mars_facts_transposed


# In[55]:


##Convert the data to an HTML table string
mars_facts_transposed_html = mars_facts_transposed.to_html()
mars_facts_transposed_html


# # Part 4: Mars Hemispheres

# Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mars' hemispheres.

# ### Part 4A--Find Cerberus Image & Title

# In[58]:


##Set up scraper for images of Mars' hemispheres, starting w/Cerberus
# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'lxml')


# In[104]:


##Find title for cerberus hemisphere image
cerberus_title = soup.find('title').text
cerberus_title = cerberus_title.split('|')
cerberus_title = cerberus_title[0]
cerberus_title


# In[93]:


##Find URL for cerberus hemisphere image
cerberus_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
cerberus_hemisphere = cerberus_hemisphere[0]
cerberus_hemisphere = cerberus_hemisphere.find_all('img', class_='wide-image')
cerberus_hemisphere = cerberus_hemisphere[0]
cerberus_hemisphere = cerberus_hemisphere['src']
cerberus_hemisphere


# In[96]:


##Save base URL to save all urls to images 
base_url = 'https://astrogeology.usgs.gov/'
cerberus_full_url = base_url + cerberus_hemisphere
cerberus_full_url


# In[105]:


#Initialize dictionary to save url image and title
hemisphere_image_urls = [
    {"title": cerberus_title, "img_url": cerberus_full_url}
]


# ### Part 4B--Find Valles Marineris Hemisphere Image & Title

# In[107]:


##Set up scraper for images of Mars' hemispheres, now Marineris
# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'lxml')


# In[108]:


##Find title for Valles Marineris hemisphere image
valles_title = soup.find('title').text
valles_title = valles_title.split('|')
valles_title = valles_title[0]
valles_title


# In[109]:


##Find URL for valles hemisphere image
valles_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
valles_hemisphere = valles_hemisphere[0]
valles_hemisphere = valles_hemisphere.find_all('img', class_='wide-image')
valles_hemisphere = valles_hemisphere[0]
valles_hemisphere = valles_hemisphere['src']
valles_hemisphere


# In[110]:


##Construct full image URL
valles_full_url = base_url + valles_hemisphere
valles_full_url


# In[112]:


##Add to dictionary
hemisphere_image_urls.append({"title": valles_title, "img_url": valles_full_url})
hemisphere_image_urls


# ### Part 4C--Find Schiaparelli Hemisphere Image & Title

# In[113]:


##Set up scraper for images of Mars' hemispheres, now Schiaparelli
# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'lxml')


# In[114]:


##Find title for Schiaparelli Hemisphere image
schiaparelli_title = soup.find('title').text
schiaparelli_title = schiaparelli_title.split('|')
schiaparelli_title = schiaparelli_title[0]
schiaparelli_title


# In[115]:


##Find URL for schiaparelli hemisphere image
schiaparelli_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
schiaparelli_hemisphere = schiaparelli_hemisphere[0]
schiaparelli_hemisphere = schiaparelli_hemisphere.find_all('img', class_='wide-image')
schiaparelli_hemisphere = schiaparelli_hemisphere[0]
schiaparelli_hemisphere = schiaparelli_hemisphere['src']
schiaparelli_hemisphere


# In[116]:


##Construct full image URL
schiaparelli_full_url = base_url + schiaparelli_hemisphere
schiaparelli_full_url


# In[117]:


##Add to dictionary
hemisphere_image_urls.append({"title": schiaparelli_title, "img_url": schiaparelli_full_url})
hemisphere_image_urls


# ### Part 4D--Find Syrtis Major Hemisphere Image & Title

# In[118]:


##Set up scraper for images of Mars' hemispheres, now Syrtis Major
# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'lxml')


# In[119]:


##Find title for Syrtis Major Hemisphere image
syrtis_title = soup.find('title').text
syrtis_title = syrtis_title.split('|')
syrtis_title = syrtis_title[0]
syrtis_title


# In[120]:


##Find URL for Syrtis Major hemisphere image
syrtis_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
syrtis_hemisphere = syrtis_hemisphere[0]
syrtis_hemisphere = syrtis_hemisphere.find_all('img', class_='wide-image')
syrtis_hemisphere = syrtis_hemisphere[0]
syrtis_hemisphere = syrtis_hemisphere['src']
syrtis_hemisphere


# In[121]:


##Construct full image URL
syrtis_full_url = base_url + syrtis_hemisphere
syrtis_full_url


# In[122]:


##Add to dictionary
hemisphere_image_urls.append({"title": syrtis_title, "img_url": syrtis_full_url})
hemisphere_image_urls


# In[ ]:




