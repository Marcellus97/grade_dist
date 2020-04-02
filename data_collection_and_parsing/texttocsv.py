import os
import re

def write_data(classes):
	print('writing the complete data')
	class_data = open('class_data.csv', 'w')
	count = 0
	sub_count = 0
	class_data.write('dept,code,section,prof_first,prof_last,A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F,W,WP,WF,I,X,Y,P,S,miami_plan?,honors?,cross_listing,campus, year,term\n')
	for c in classes:
		try:
			cross = 'none'
			meta = c['meta_grades']
			if len(meta) == 3:
				cross = c['meta_grades'][2]
			line = c['dept'] + ',' + c['code'] + ',' + c['section'] + ',' + c['prof_first'] + ',' + c['prof_last'] + ','
			for g in c['grades']:
				line += g + ','
			line += meta[0] + ',' + meta[1] + ',' + cross + ',' +  c['campus'] + ',' + c['year'] + ',' + c['term'] + '\n'
			
			if sub_count > 1000:
				print(count)
				sub_count = 0
			sub_count += 1
			count += 1
			class_data.write(line)
		except:
			print('Some error, probably out of range. Printing class...')
			print(c)
	class_data.close()

semesters = os.listdir('chunks')
classes = []
for sem in semesters:
	print('starting: ' + sem) 
	pages = os.listdir('chunks/' + sem)
	for p in pages:
		if not p.endswith('.txt'): #ignore non text files
			continue
		txt = open('chunks/' + sem + '/' + p, 'r')
		lines = txt.readlines()
		
		if len(lines) < 3: #must be a garbage page
			continue		
		match = re.search('\w+ Campus$', lines[2])		
		if not match:
			continue
		campus = lines[2][match.start() : -8].strip()
		
		i = 0
		while (i < len(lines)): 
			if re.search('^[A-Z][A-Z][A-Z] [0-9][0-9][0-9][A-Z]*', lines[i]): #course start line
				info = lines[i].split(' ')
				course_type = info[0].strip()
				course_number = info[1].strip()
				course_section = info[2].strip()
				prof_last = info[3].strip()
				prof_first = info[4].strip()
				j = i + 1 # need new increment, because we cannot gaurantee length yet
				meta_grades = []
				grades = []
				while re.search('^[A-Z][0-9]*$', lines[j]):
					meta_grades.append(lines[j].strip())
					j += 1
				j += 17 #skip garbage
				for k in range(0, 21):
					grades.append(lines[j + k].strip())
				#i = j #add j, 23 is guaranteed at the end of loop
				
				mydict = {}
				mydict['dept'] = course_type
				mydict['code'] = course_number
				mydict['section'] = course_section
				mydict['prof_first'] = prof_first
				mydict['prof_last'] = prof_last
				mydict['grades'] = grades
				mydict['meta_grades'] = meta_grades
				mydict['campus'] = campus
				mydict['year'] = sem[-4:]
				mydict['term'] = sem[:-4]
				classes.append(mydict) 
			i += 1	
		txt.close()
write_data(classes)
