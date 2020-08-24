import re
import pprint


domain = 'https://wiprodigital.com'

domain_urls = []
external_urls = []
static_images = []
static_css = []
static_js = []

pattern_for_domain_urls = re.compile(r'https://wiprodigital\.com/?([a-zA-Z0-9-/_.]*)')
pattern_static_css_and_js = re.compile(r'https?://([a-zA-Z0-9.=-]*)/.*\.(js|css)[a-zA-Z0-9-_=?.]*')
pattern_static_images = re.compile(r'(https?://[a-zA-Z0-9.=-]*)/.*\.(png|jpg|jpeg|gif|svg)[a-zA-Z0-9-_=?.]*')

# open and read the file
with open('html.txt') as f:
    contents = f.read()
    pattern = pattern_static_images
    match_for_domain_urls = pattern.finditer(contents)
    for url in match_for_domain_urls:
        print(url.group(0))
        domain_urls.append(url.group(0))


domain_urls_set = set()
for url in domain_urls:
    if url[-1] == '/':
        url = url[0:-1]
        domain_urls_set.add(url)

domain_urls = list(domain_urls_set)
domain_urls.sort()

pprint.pprint(domain_urls)
