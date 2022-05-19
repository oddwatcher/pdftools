import PyPDF2 as pdf
oddout = open("./second.pdf",'wb')
evenout = open("./first.pdf",'wb')
while True:
    try:
        din = input("The file to print:\n")
        open(din,"r")
        break
    except:
        print("file not exist")
pdfin = pdf.PdfFileReader(din)
lastpage = pdf.PdfFileReader("./lastpage.pdf")
pdfodd = pdf.PdfFileWriter()
pdfeven = pdf.PdfFileWriter()
total = pdfin.numPages
for i in range(0,total,2):
    page= pdfin.getPage(i)
    pdfeven.addPage(page)
total = total-1

if total%2 ==0:
    tail = total-1
    pdfodd.addPage(lastpage.getPage(0))
else:
    tail = total

for i in range(tail,0,-2):
    page= pdfin.getPage(i)
    pdfodd.addPage(page)

pdfeven.write(evenout)
pdfodd.write(oddout)
evenout.close()
oddout.close()
print("Even:%d,Odd:%d,Total:%d",pdfeven.getNumPages(),pdfodd.getNumPages(),total+1)

