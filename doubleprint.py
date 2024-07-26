import PyPDF2 as pdf
from pathlib import Path
f = 1
flag = input("Inkjet/Laser? type 0/1")
files = []
lastpage = pdf.PdfReader("./lastpage.pdf")
pdfodd = pdf.PdfWriter()
pdfeven = pdf.PdfWriter()
outputpath = Path(input("Output path:"))
if not outputpath.exists():
    Path.mkdir(outputpath)
while (True):
    while True:
        din = Path(input("The PDF to process").lstrip('"').rstrip('"'))
        if din.exists():
            if din.is_dir():
                print("will convert all pdfs")
                files = list(din.glob("*.pdf"))
                break
            else:
                if str(din).split('.')[1] == "pdf":
                    files.append(din)
                break
        print("Path not exist")
    for f in files:
        pdfin = pdf.PdfReader(str(f))

        total = len(pdfin.pages)
        for i in range(0, total, 2):
            page = pdfin.pages[i]
            pdfeven.add_page(page)

        if (flag == '1'):
            if total % 2 != 0:
                tail = total-2
                pdfodd.add_page(lastpage.pages[0])
            else:
                tail = total-1
            for i in range(tail, 0, -2):
                page = pdfin.pages[i]
                pdfodd.add_page(page)
        else:
            for i in range(1, total, 2):
                page = pdfin.pages[i]
                pdfodd.add_page(page)
            if (total+1) % 2 == 0:
                pdfodd.add_page(lastpage.pages[0])

        pdfodd.write(outputpath/('even'+str(f.parts[-1])))
        pdfeven.write(outputpath/('odd'+str(f.parts[-1])))

        outstr = "Even:%d,Odd:%d,Total:%d,File:%s" % (
            len(pdfeven.pages), len(pdfodd.pages), total+1, f)
        print(outstr)
