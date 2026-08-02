#########################Text Extraction from PDF using PyMuPDF (fitz)#########################
import fitz

docs = fitz.open("sample_fonts_test.pdf")

for page_number,page in enumerate(docs,start=1):

    page_dict=page.get_text("dict")
    for block in page_dict["blocks"]:
        if block["type"]==0:
            for line in block["lines"]:
                for span in line["spans"]:
                    text=span["text"]
                    font=span["font"]
                    size=span["size"]
                    print(f"Page {page_number}: Text: {text}, Font: {font}, Size: {size}")



