from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

#output_string = StringIO()
output = open('pdfminer_example_Spring2015.txt', 'w') 

with open('pdfs/Spring2015.pdf', 'rb') as in_file:
	parser = PDFParser(in_file)
	doc = PDFDocument(parser)
	rsrcmgr = PDFResourceManager()
	device = TextConverter(rsrcmgr, output, laparams=LAParams())
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	counter = 0
	for page in PDFPage.create_pages(doc):
		interpreter.process_page(page)
		counter += 1
		print(counter)	
	
