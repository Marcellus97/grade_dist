#chunk each text file by page, using the LF character. 
#Each respective pdf folder will have a collection of each page.txt file

import os

def writePage(file_name, semester,  page_arr):
	page = open('chunks/' + semester + '/' + file_name, 'w')
	page.write('test')
	for p in page_arr:
		page.write(p)
	page.close()

file_names = os.listdir('chunks')

for semester in file_names:
	txt_file = open('parsed_txt/' + semester+ '_parsed.txt', 'r')
	
	lines = txt_file.readlines()
	page_count = 1
	page = []

	for line in lines:
		if line[0] == '\f': # first char is \f. This splits the page 
			writePage('page' + str(page_count) + '.txt', semester, page)
			page = []
			page.append(line[1:]) #This line should actually be for the next page
			page_count += 1
		else:
			page.append(line)
	writePage('page' + str(page_count) + '.txt', semester, page) #append the final page

	txt_file.close()

