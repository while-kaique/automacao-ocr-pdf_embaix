# ocr_pdf.py
from pdf2image import convert_from_path
import pytesseract
import sys

pdf_path = sys.argv[1]
output_path = sys.argv[2] if len(sys.argv) > 2 else "output.txt"

pages = convert_from_path(pdf_path, dpi=300)
texto_extraido = ""

for i, page in enumerate(pages):
    texto = pytesseract.image_to_string(page, lang="por")
    texto_extraido += f"\n--- Página {i+1} ---\n{texto}"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(texto_extraido)
