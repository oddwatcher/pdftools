import PyPDF2 as pdf
merger = pdf.PdfWriter()

while True:
    while True:
        din = input("files to merge:")
        din = din.lstrip("\"")
        din = din.rstrip("\"")
        try:
            open(din,"r")
            break
        except:
            print("file not exist\n")

    if(din == "fin"):
            break
        
    reader=pdf.PdfReader(din)
    num_page=len(reader.pages)
    for i in range(0,num_page):
        page = reader.pages[i]
        merger.add_page(page)
    print("current pages:{}\n".format(len(merger.pages)))    

print("current pages:{}\n".format(len(merger.pages)))

merger.write("./output.pdf")
