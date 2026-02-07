"""
PDF to Image Converter for Portfolio

This script converts all PDF files in the static/images folder to JPG images.

REQUIREMENTS:
Run this command first to install dependencies:
    pip install pdf2image Pillow

On Windows, you also need to install Poppler:
1. Download from: https://github.com/osber/poppler-windows/releases
2. Extract to C:\poppler
3. Add C:\poppler\bin to your system PATH

Alternatively, use this simpler approach:
    pip install PyMuPDF

Then run: python convert_pdfs.py
"""

import os
import glob

def convert_with_pymupdf():
    """Convert PDFs using PyMuPDF (simpler, no external dependencies)"""
    try:
        import fitz  # PyMuPDF

        images_folder = os.path.join(os.path.dirname(__file__), 'static', 'images')
        pdf_files = glob.glob(os.path.join(images_folder, '*.pdf'))

        print(f"Found {len(pdf_files)} PDF files to convert...")

        for pdf_path in pdf_files:
            filename = os.path.basename(pdf_path)
            name_without_ext = os.path.splitext(filename)[0]

            # Create output path - replace spaces with underscores, lowercase
            output_name = name_without_ext.lower().replace(' ', '_') + '.jpg'
            output_path = os.path.join(images_folder, output_name)

            # Skip if already converted
            if os.path.exists(output_path):
                print(f"  ✓ {output_name} already exists, skipping...")
                continue

            try:
                # Open PDF
                doc = fitz.open(pdf_path)
                page = doc[0]  # First page

                # Render at high DPI for quality
                zoom = 2.0  # 2x zoom for better quality
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat)

                # Save as JPEG
                pix.save(output_path)
                doc.close()

                print(f"  ✓ Converted: {filename} → {output_name}")

            except Exception as e:
                print(f"  ✗ Error converting {filename}: {e}")

        print("\n✅ Conversion complete!")
        print("\nYour images are ready in: static/images/")
        return True

    except ImportError:
        print("PyMuPDF not installed. Installing now...")
        os.system('pip install PyMuPDF')
        print("Please run this script again after installation.")
        return False


def list_available_images():
    """List all available JPG images after conversion"""
    images_folder = os.path.join(os.path.dirname(__file__), 'static', 'images')
    jpg_files = glob.glob(os.path.join(images_folder, '*.jpg'))

    print("\n📚 Available portfolio images:")
    print("-" * 40)

    for img in sorted(jpg_files):
        filename = os.path.basename(img)
        print(f"  /static/images/{filename}")

    print("-" * 40)
    print(f"Total: {len(jpg_files)} images")


if __name__ == '__main__':
    print("=" * 50)
    print("📄 PDF to Image Converter")
    print("=" * 50)

    success = convert_with_pymupdf()

    if success:
        list_available_images()
        print("\n🎉 Now restart your Flask app to see the changes!")
