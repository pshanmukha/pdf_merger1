#import neccessary library 
from PyPDF2 import PdfFileReader, PdfFileMerger

#! First read both pdf files
pdf_file1 = PdfFileReader(" ") #add pdf file1 in quotes
pdf_file2 = PdfFileReader(" ") #add pdf file2 in quotes

#!Create a pdffilemerger object
output = PdfFileMerger()

#!append both the pdf reader object in to it
output.append(pdf_file1)
output.append(pdf_file2)

#!save the merge pdf
output.write("merged.pdf")
