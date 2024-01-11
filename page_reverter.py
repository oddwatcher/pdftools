import PyPDF2 as pdf
din = input("The PDF to process\n")
while True:
    try:
        open(din, "r")
        break
    except:
        print("file not exist")
        din = input("The PDF to process\n")
pdfin = pdf.PdfReader(din)
total = len(pdfin.pages)
out = pdf.PdfWriter()
for i in range(total-1,-1,-1):
    page = pdfin.pages[i]
    out.add_page(page)
outfile = open("./output/reverted.pdf", 'wb')
out.write(outfile)
outfile.close()
print("Total Pages: {}\n".format(total))