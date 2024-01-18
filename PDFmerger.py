import PyPDF2 as pdf
merger = pdf.PdfWriter()

while True:
    
    din = input("files to merge:")
    din = din.lstrip("\"")
    din = din.rstrip("\"")
    print(din)
    try:
        open(din,'r')
        try:
            reader=pdf.PdfReader(din)
            num_page=len(reader.pages)
            for i in range(0,num_page):
                page = reader.pages[i]
                merger.add_page(page)
        except:
            print("something is wrong with pdf file\n")
    except: 
        if(din == "fin"):
            break
        print("File not found,Retry")
        print("to stop type fin\n")
        print("current pages:{}\n".format(len(merger.pages)))


print("current pages:{}\n".format(len(merger.pages)))

merger.write("./output.pdf")
