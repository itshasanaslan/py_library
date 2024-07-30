from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import os
from pathlib import Path

RECURSIVE = False

if len(sys.argv) < 3:
    print("Correct usage is this")
    print("program.exe dir/input.pdf output.pdf")
    exit()

file_to_open = sys.argv[1]
if not os.path.exists(file_to_open):
    print("File not found: " + file_to_open)
    exit()

if len(sys.argv) >= 3 and "recursive" in sys.argv:
    RECURSIVE = True
    print("Recursion for per page is activated.")

def recursive(out_dir, stop_at):
    pdf_file = PdfFileReader(open(file_to_open, "rb"))
    for i in range(stop_at):
        _filename = os.path.join(out_dir, str(i) + ".pdf")
        print(_filename)
        output = PdfFileWriter()
        start, end = i, i

        for j in range(start, end):
            output.addPage(pdf_file.getPage(j+1))

        with open(_filename, 'wb') as outputStream:
            output.write(outputStream)
        print("File is saved as " + _filename)


def crop(out_dir, pdf_file, start_page, end_page, out_name = False):
    try:
        out_name = os.path.join(out_dir, sys.argv[2]) if not out_name else out_name 
        output = PdfFileWriter()
        


        for i in range(start_page, end_page):
            output.addPage(inputpdf.getPage(i))

        with open(out_name, "wb") as outputStream:
            output.write(outputStream)
        print("File saved as", out_name)
    except Exception as wtf:
        print(wtf)


try:
    actual_path = Path(file_to_open)
    inputpdf = PdfFileReader(open(file_to_open, "rb"))
    out_dir = actual_path.parent
    
    if not RECURSIVE:
            start = int(input("Starting page: "))
            end = int(input("Ending page: ")) + 1       
            crop(out_dir, inputpdf, start, end)
            
    # recursive
    else:
        until_page = int(input("Stop at page: "))
        interval = int(input("Page count per file: "))
        for i in range(until_page):
            crop(out_dir, inputpdf, i, i + interval, out_name = str(i) + '.pdf')

except Exception as wtf:
    print(wtf)

