import os

csv_format = 'Class code,Class name,Section,Dept code,Dept name,Prof,A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F,W,WP,WF,I,X,S,Miami Plan?,Honors?,Cross Listing code,Year,Term,Campus'
txt_file_names = os.listdir('parsed_txt/')

#master_dict = 

for file_name in txt_file_names:
	txt_file = open('parsed_txt/' + file_name, 'r')
	lines = txt_file.readlines()
	
	full_data = []

	table_of_contents = True
	current_campus = lines[1]
	index = 0	

	while index < len(lines)

	txt_file.close()
	break

def chunkPages():
	return 0	

