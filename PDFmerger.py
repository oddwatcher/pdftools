import PyPDF2 as pdf
while True:
    try:
        din = input("files to merge:")
        PDFin = open(din,'r')
        break
    except:
        print("File not found,Retry")
buff = pdf.PdfFileMerger()
buff.merge()
