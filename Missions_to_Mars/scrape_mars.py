import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #initialize dictionary for scraped data results
    mars_scrape = {}




    ### NASA Mars News
    #URL definitions
    news_url = "https://redplanetscience.com/"
    browser.visit(news_url)
    time.sleep(1)

    # Scrape page into Soup
    news_html = browser.html
    soup = bs(news_html, "html.parser")

    # ID the article to be scraped
    news_article = soup.find('div', id='news')

    # Get the latest article title
    news_title = news_article.find('div', class_='content_title').get_text()

    # Get the latest article title
    news_p = news_article.find('div', class_='article_teaser_body').get_text()

    mars_scrape['news_title'] = news_title
    mars_scrape['news_p'] = news_p






    ### JPL Mars Space Images - Featured Image
    #URL definitions
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)
    time.sleep(1)

    # Scrape page into Soup
    image_html = browser.html
    soup = bs(image_html, "html.parser")

    # Find path to image
    img_find = soup.find('div', class_='header')

    #find the image to be scraped
    relative_image_path = img_find('img')[1]["src"]
    featured_image_url = image_url + relative_image_path

    mars_scrape['featured_image_url'] = featured_image_url





    ### Mars Facts
    #URL definitions
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    time.sleep(1)

    tables_df = pd.read_html(facts_url)[1]
    #tables_df
    mars_facts = tables_df.to_html(header=True)

    mars_scrape['mars_facts'] = mars_facts






    ## Hemispheres
    #variables
    ints = [0,1,2,3]
    url_list = ['https://marshemispheres.com/cerberus.html','https://marshemispheres.com/schiaparelli.html','https://marshemispheres.com/syrtis.html','https://marshemispheres.com/valles.html']
    hemi_list = []
    hemi_dict = {}

    for i in ints:
        # Set up Splinter
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)

        #URL definitions
        hemi_url = url_list[i]
        browser.visit(hemi_url)
        time.sleep(1)

        # Scrape page into Soup
        hemi_html = browser.html
        soup = bs(hemi_html, "html.parser")

        # Get image
        hemi_img_find = soup.find('div', id='wide-image')
        hemi_title_find = soup.find('div', class_='cover')

        #find the image to be scraped
        hemi_image_path = hemi_img_find.find_all('img')[1]["src"]
        hemi_title = hemi_title_find.find_all('h2')[0].text
        image_url = hemi_url + hemi_image_path
        hemi_dict = {'title': hemi_title,'img_url':image_url}
        hemi_list.append(hemi_dict)
    
    browser.quit()

    mars_scrape['hemi_list'] = hemi_list
    return mars_scrape

