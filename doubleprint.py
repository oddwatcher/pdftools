import PyPDF2 as pdf
oddout = open("./second.pdf",'wb')
evenout = open("./first.pdf",'wb')
din = "C:/Users/scien/Desktop/1.pdf"
while True:
    try:
        open(din,"r")
        break
    except:
        print("file not exist")
        din = input("The PDF to process")
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
outstr = "Even:%d,Odd:%d,Total:%d" %(pdfeven.getNumPages(),pdfodd.getNumPages(),total+1)
print(outstr)
input("press to restart\n")

