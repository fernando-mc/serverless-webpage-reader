import requests
from bs4 import BeautifulSoup

# Create a variable with the url
url = 'https://www.fernandomc.com'
test_url = 'https://theintercept.com/2017/12/24/star-wars-last-jedi-class-politics/'
# Use requests to get the contents
r = requests.get(test_url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'html.parser')


soup.find_all('p')

.replace('<span style="font-weight: 400">','')