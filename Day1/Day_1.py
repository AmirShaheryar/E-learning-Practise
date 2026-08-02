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


#########################Image Extraction from PDF using PyMuPDF (fitz)#########################


import fitz
import os

doc=fitz.open("Img.pdf")
os.makedirs("extracted_images",exist_ok=True)

for page_number,page in enumerate(doc,start=1):
    image_list=page.get_images(full=True)
    for image_index,image in enumerate(image_list,start=1):

        xref=image[0]
        base_image=doc.extract_image(xref)
        image_bytes=base_image["image"]
        image_ext=base_image["ext"]

        file_path=os.path.join("extracted_images",f"page_{page_number}_image_{image_index}.{image_ext}")
        with open(file_path,"wb") as image_file:
            image_file.write(image_bytes)
        print(f"Saved image {image_index} from page {page_number} as {file_path}")