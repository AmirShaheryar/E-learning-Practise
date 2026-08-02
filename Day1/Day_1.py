import fitz

doc = fitz.open("sample_fonts_test.pdf")  

for page_num, page in enumerate(doc, start=1):
    page_dict = page.get_text("dict")
    
    for block in page_dict["blocks"]:
        if block["type"] == 0:
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"]
                    font = span["font"]
                    size = span["size"]
                    print(f"Page {page_num} [{font} {size}pt]: {text}")