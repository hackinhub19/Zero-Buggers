import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('testing.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
no=pdfReader.numPages
f=open("codefile.txt","w+")
print(no) 
for i in range(0,no):
    # creating a page object
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    
    
    f.write(pageObj.extractText())
# closing the pdf file object
pdfFileObj.close()