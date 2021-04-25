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

```

#### Scrapy shell

```python
scrapy shell http://quotes.toscrape.com/
scrapy shell http://quotes.toscrape.com/ -s USER_AGENT='custom user agent' --nolog
```

Scrapy Shell for mulitple urls

```python
>>> scrapy shell

import re, os, json
from scrapy import Request
from importlib import reload

req = Request('yoururl.com', headers={"header1":"value1"})
fetch(req)
```





## Xpath

useful xpath website: [http://zvon.org/comp/r/tut-XPath_1.html#Pages~List_of_XPaths](http://zvon.org/comp/r/tut-XPath_1.html#Pages~List_of_XPaths)

Get elment **by text it contains**

```python
//*[text()='match']
//*[contains(text(),'match')]
//*[normalize-space(text())='match']

```

Get element, **by attribute value**

```python
//*[@class="quote"]
//*[@itemprop="keywords"]
```

Get element, that **contains**

```
//*[contains(@class, 'property-item-wrapper')]
```

Get element, that does **not contain**

```
//section[not(@class="property_listing")]
```

Get **sibling** element

```python
//*[@id="product_description"]/following-sibling::p/text()
```

Get multiple elements, using **or**

```
//*[@id="description" or @id="address" or @id="detail"]/descendant::*/text()
//*[@class="article"]|//*[@class="section-head test"]
```

Get **text** of element

```python
//*[@class="text"]/text()
.xpath('//body/descendant::*/text()').getall()  # text of all subelements
.xpath('//h1//text()').get() -> str             # text of all subelements
.xpath('//body//text()').getall() -> list		    # all text from html body
.xpath('string(//body[1])').get() -> str        # all text from html body
```

Get **attribute value** of element

```python
//*[@itemprop="keywords"]/@content
```

Other

```python
# get first 
//*[@class="login"/a[1]] # get second a element
```



sample from zyte

https://www.zyte.com/blog/xpath-tips-from-the-web-scraping-trenches/

```python
from scrapy import Selector
sel = Selector(text='<a href="#">Click here to go to the <strong>Next Page</strong></a>')
xp = lambda x: sel.xpath(x).extract() # let's type this only once
xp('//a//text()') # take a peek at the node-set
	>>> [u'Click here to go to the ', u'Next Page']
xp('string(//a//text())')  # convert it to a string
	>>> [u'Click here to go to the ']
```



#### Next Page

```python
next_page = response.xpath('//ul[@class="pagination"]//*[@rel="next"]/@href').get()
absolute_url = response.urljoin(next_page)
```



#### Modify response object

https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request.replace

```python
# remove new lines from 
response = response.replace(body = response.text.replace('\n', ''))
# remove html comments
response = response.replace(body = re.sub('<!--[^(-->)]+-->', '', response.text))

# replace part of a response
response = response.replace(body = response.text.replace(
  	response.xpath('//*[@class="rh_property__sidebar"]').get(), ''
)
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


