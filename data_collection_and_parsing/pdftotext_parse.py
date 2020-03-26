import os

pdf_files = os.listdir('pdfs/')

for pdf_filename in pdf_files:
	output_name = 'pdf_to_text_v2/' + pdf_filename[:-3] + 'txt'
	os.system('pdftotext ' + 'pdfs/' + pdf_filename + ' ' + output_name)
	print(pdf_filename)

