import fitz
import os

pdf_path = r'static/images/new_PORTFOLIO PG28.pdf'
jpg_path = r'static/images/portfolio_pg28.jpg'

# Delete existing jpg if it exists
if os.path.exists(jpg_path):
    os.remove(jpg_path)
    print(f"Deleted old {jpg_path}")

# Convert PDF to JPG
doc = fitz.open(pdf_path)
page = doc[0]
mat = fitz.Matrix(2.0, 2.0)
pix = page.get_pixmap(matrix=mat)
pix.save(jpg_path)
doc.close()

print(f"Successfully converted {pdf_path} to {jpg_path}")
print(f"New file size: {os.path.getsize(jpg_path) / 1024:.1f} KB")
