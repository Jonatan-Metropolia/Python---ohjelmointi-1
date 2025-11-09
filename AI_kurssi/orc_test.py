import os

from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


image_name = input(r"Enter file name.extencion (png, pdf etc): ")
image_path = rf"C:\Users\Käyttäjä\OneDrive - Metropolia Ammattikorkeakoulu Oy\Desktop\jutut\img_to_text\input\{image_name}"
output_path = rf"C:\Users\Käyttäjä\OneDrive - Metropolia Ammattikorkeakoulu Oy\Desktop\jutut\img_to_text\output\{image_name}.txt"

#Suorita OCR
text = pytesseract.image_to_string(Image.open(image_path))

print("Tunnistettu teksti:\n")
print(text)

#tallennetaan tulos tiedostoon
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"\n Teksti tallennettu tiedostoon: {output_path}")
