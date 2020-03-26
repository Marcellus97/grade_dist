from bs4 import BeautifulSoup
import requests
import html.parser

ELEMENT_ID = 'contentcontainer'
BASE_URL = 'https://web.archive.org/web/20160217105911/http://www.units.miamioh.edu/reg/gradedist/documents/'

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.text, 'html.parser')
anchors = soup.find_all('a')

links = [ref.get('href') for ref in anchors]

# remove other undesrired links
links = links[5:-1]

output = open('links.txt', 'w')
for l in links:
	output.write('{}{}\n'.format(BASE_URL, l))
output.close()

