#!/usr/bin/python

from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Path of the pdf
PDF_file = "<name-of-the-file>"

# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500)

# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pages:
    filename = f"page_{image_counter}.jpg"

    # Save the image of the page in system
    page.save(filename, 'JPEG')

    # Increment the counter to update filename
    image_counter = image_counter + 1

# Variable to get count of total number of pages
filelimit = image_counter-1

# Creating a text file to write the output
outfile = "out_text.txt"

f = open(outfile, "a")

# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
    filename = "page_"+str(i)+".jpg"

    # Recognize the text as string in image using pytesserct
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')
    f.write(text)

# Close the file after writing all the text.
f.close()
