import os
import requests

links = []
link_file = open('links.txt','r')
print('Downloading files...')

count = 0
for link in link_file:
	r = requests.get(link)
	clean_name = link[109:].strip().replace('%20','')
	with open('pdfs/' + clean_name, 'wb') as file:
		file.write(r.content)
	count+=1
	print('File {} complete'.format(count))
print('Download complete!')
