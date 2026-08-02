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

#########################Math Extraction from PDF using PyMuPDF (fitz)#########################

import re

MATH_REGEX = re.compile(r'(\$\$?[\s\S]+?\$\$?|\\\(.*?\\\)|\\\[.*?\\\]|\\int|\\frac|\\sum|\\sqrt)')
MATH_FONTS = ["math", "cmsy", "cmex", "symbol", "stix", "cambriamath"]
UNICODE_MATH = ["∫", "∑", "∏", "√", "∂", "∇", "≤", "≥", "≠", "±", "≈", "∞", "α", "β", "θ", "π"]

def analyze_span(text, font_name=""):
    """Determines if a span contains math and identifies WHICH rule caught it."""
    reasons = []
    
    if MATH_REGEX.search(text):
        reasons.append("Matched LaTeX Regex Pattern")
        
    if any(kw in font_name.lower() for kw in MATH_FONTS):
        reasons.append(f"Matched Math Font ('{font_name}')")
        
    if any(char in text for char in UNICODE_MATH):
        reasons.append("Matched Unicode Math Character")
        
    is_math = len(reasons) > 0
    return is_math, reasons

test_spans = [
    {"text": "Welcome to Chapter 3: Quantum Mechanics", "font": "Helvetica-Bold"},
    {"text": "The energy equation is $E = mc^2$ in physics.", "font": "Times-Roman"},
    {"text": "∫ (2x + 1) dx = x^2 + x + C", "font": "Times-Roman"},
    {"text": "a^2 + b^2 = c^2", "font": "CMSY10-Math"}
]


print("\n--- MATH EXTRACTION PRACTICE LAB ---\n")

for idx, span in enumerate(test_spans, start=1):
    text = span["text"]
    font = span["font"]
    
    is_math, reasons = analyze_span(text, font)
    
    print(f"Sample #{idx}:")
    print(f"  Text:   '{text}'")
    print(f"  Font:   '{font}'")
    print(f"  Result: {' MATH DETECTED' if is_math else ' NORMAL TEXT'}")
    if is_math:
        print(f"  Why:    {', '.join(reasons)}")
    print("-" * 50)