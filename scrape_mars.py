from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def scrape():

    mars_data = {}

    # # Scape NASA Mars News
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    news_title = soup.find('div', class_="content_title").text.strip()
    news_p = soup.find(class_="rollover_description_inner").text.strip()


    # ## JPL Mars Space Images - Featured Image
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    browser.click_link_by_id('full_image')

    relative_url = soup.find_all('img')[3]["src"]
    featured_image_url = url + relative_url

    browser.quit()


    # # Mars Weather
    url = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()


    # # Mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    tables
    df = tables[1]
    df.columns = ['Index', 'Measure']
    df.to_html('mars_facts')
    


    # # Mars Hemispheres

    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #browser = Browser('chrome', **executable_path, headless=False)


    # In[53]:


    #url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    #browser.visit(url)


    # In[54]:


    #browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')


    # In[55]:


    #title_1 = soup.find('div', class_="container").find('h2', class_="title")
    #print(title_1)


    # In[56]:


    #browser.click_link_by_partial_text('Sample')


    # In[57]:


    #relative_url_1 = soup.find_all('img')
    #featured_image_url_1 = url + relative_url_1
    #print(featured_image_url_1)


    # In[58]:


    #print(relative_url_1)


    # In[ ]:





    # In[59]:


    #url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


    # In[60]:


    #response = requests.get(url)


    # In[61]:


    #soup = bs(response.text, 'html.parser')
    #print(soup.prettify())


    # In[62]:


    #relative_url_1 = soup.find_all('img', class_="thumb")[0]["src"]
    #featured_image_url_1 = url + relative_url_1
    #print(featured_image_url_1)


    # In[63]:


    #print(relative_url_1)

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]

    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p
    mars_data["featured_image_url"] = featured_image_url
    mars_data["mars_weather"] = mars_weather
    #mars_data["mars_facts"] = html_table
    mars_data["mars_hemisphere"] = hemisphere_image_urls

    return mars_data