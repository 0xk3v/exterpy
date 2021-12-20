from pdf2image import convert_from_path


pdfs = r"file.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = f"Page_{i}.jpg"
    page.save(image_name, "JPEG")
    i += 1
