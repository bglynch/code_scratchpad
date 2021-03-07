# Scrapy Cheatsheet



## Get started

```bash
pip install scrapy
scrapy startproject <project_name>
scrapy genspider <name> <domain_url> # scrapy genspider login quotes.toscrape.com
scrapy list
scrapy crawl <spider_name>
#  scrapy crawl <name> -o items.csv
#  scrapy crawl <name> -o items.json
#  scrapy crawl <name> -o items.xml

scrapy shell http://quotes.toscrape.com/
scrapy shell http://quotes.toscrape.com/ -s USER_AGENT='custom user agent' --nolog

```



## Xpath

website: [http://zvon.org/comp/r/tut-XPath_1.html#Pages~List_of_XPaths](http://zvon.org/comp/r/tut-XPath_1.html#Pages~List_of_XPaths)

```python

# text that contains
//*[text()='match']
//*[contains(text(),'match')]
//*[normalize-space(text())='match']

# get element by attribte value
//*[@class="quote"]

# get text value
//*[@class="text"]/text()
//h1/descendant::*/text()  # text of all subelements

# class that contains
//*[contains(@class, 'property-item-wrapper')]

# get attribute value
//*[@itemprop="keywords"]/@content

# get sibling
//*[@id="product_description"]/following-sibling::p/text()
    
# using or
//*[@id="description" or @id="address" or @id="detail"]/descendant::*/text()
//*[@class="article"]|//*[@class="section-head test"]
    
# not contains
//section[not(@class="property_listing")]

# get first 
//*[@class="login"/a[1]] # get second a element
```



## Selenium with Scrape

https://selenium-python.readthedocs.io/installation.html

`pip install selenium`



```python
from selenium import webdriver

# create driver
driver = webdriver.Chrome('./chromedriver')

# get webpage
driver.get('http://books.toscrape.com/')

driver.title          # --> get page title
driver.current_url    # --> get page url
driver.page_source    # --> get page html

# use scrapy selector to get data from html
from scrapy.selector import Selector
sel = Selector(text=driver.page_source)
sel.xpath('//h1/text()').get()

# click nect page button
next = driver.find_element_by_xpath('//*[@class="next"]/a')
next.click()

# fill in form
driver.find_element_by_xpath('//*[@id="username"]').click()
driver.find_element_by_xpath('//*[@id="password"]').click()
driver.find_element_by_xpath('//*[@id="password"]').send_keys('pass')
driver.find_element_by_xpath('//*[@id="username"]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('user')
driver.find_element_by_xpath('//*[@value="Login"]').click()

# use different keyboard keys
from selenium.webdriver.common.keys import Keys
driver.find_element_by_xpath('//*[@id="password"]').send_keys('pass')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.RETURN)

# close the driver
driver.close()
```











