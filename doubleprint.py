import PyPDF2 as pdf
f = 1
flag = input("Inkjet/Laser? type 0/1")
while (True):
    din = f'C:/Users/Liziq/Desktop/{str(f)}.pdf'
    while True:
        try:
            open(din, "r")
            break
        except:
            print("file not exist")
            din = input("The PDF to process")
    pdfin = pdf.PdfFileReader(din)
    lastpage = pdf.PdfFileReader("./lastpage.pdf")
    pdfodd = pdf.PdfFileWriter()
    pdfeven = pdf.PdfFileWriter()
    total = pdfin.numPages
    for i in range(0, total, 2):
        page = pdfin.getPage(i)
        pdfeven.addPage(page)
    
    if (flag == '1'):
        if total % 2 != 0:
            tail = total-2
            pdfodd.addPage(lastpage.getPage(0))
        else:
            tail = total-1
        for i in range(tail, 0, -2):
            page = pdfin.getPage(i)
            pdfodd.addPage(page)
    else:
        for i in range(1, total-1, 2):
            page = pdfin.getPage(i)
            pdfodd.addPage(page)
        if (total+1) %2 !=0:
            pdfodd.addPage(lastpage.getPage(0))
    oddout = open(f"./output/{str(f)}second.pdf", 'wb')
    evenout = open(f"./output/{str(f)}first.pdf", 'wb')
    pdfeven.write(evenout)
    pdfodd.write(oddout)
    evenout.close()
    oddout.close()
    outstr = "Even:%d,Odd:%d,Total:%d,File=%s" % (
        pdfeven.getNumPages(), pdfodd.getNumPages(), total+1, f)
    print(outstr)
    input("press to restart\n")
    f = f+1
