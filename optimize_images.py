"""
Image Optimizer for Portfolio

This script compresses JPG images to reduce file size while maintaining quality.
Run this once to optimize all portfolio images.

Usage: python optimize_images.py
"""

import os
from PIL import Image

def optimize_images():
    images_folder = os.path.join(os.path.dirname(__file__), 'static', 'images')

    # Target max dimensions (A3 at 150 DPI is sufficient for web)
    MAX_WIDTH = 2000
    MAX_HEIGHT = 1500
    QUALITY = 85  # JPEG quality (85 is good balance of quality/size)

    jpg_files = [f for f in os.listdir(images_folder) if f.lower().endswith('.jpg')]

    print(f"Found {len(jpg_files)} JPG files to optimize...")
    print("-" * 50)

    total_saved = 0

    for filename in sorted(jpg_files):
        filepath = os.path.join(images_folder, filename)
        original_size = os.path.getsize(filepath)

        try:
            with Image.open(filepath) as img:
                # Get original dimensions
                orig_width, orig_height = img.size

                # Calculate new dimensions if needed
                ratio = min(MAX_WIDTH / orig_width, MAX_HEIGHT / orig_height, 1.0)

                if ratio < 1.0:
                    new_width = int(orig_width * ratio)
                    new_height = int(orig_height * ratio)
                    img = img.resize((new_width, new_height), Image.LANCZOS)

                # Convert to RGB if necessary (for JPEG)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')

                # Save with optimization
                img.save(filepath, 'JPEG', quality=QUALITY, optimize=True)

                new_size = os.path.getsize(filepath)
                saved = original_size - new_size
                total_saved += saved

                if saved > 0:
                    print(f"✓ {filename}: {original_size/1024:.0f}KB → {new_size/1024:.0f}KB (saved {saved/1024:.0f}KB)")
                else:
                    print(f"  {filename}: Already optimized")

        except Exception as e:
            print(f"✗ {filename}: Error - {e}")

    print("-" * 50)
    print(f"Total saved: {total_saved/1024/1024:.2f} MB")
    print("✅ Optimization complete!")


if __name__ == '__main__':
    # Check if Pillow is installed
    try:
        from PIL import Image
        optimize_images()
    except ImportError:
        print("Installing Pillow...")
        os.system('pip install Pillow')
        print("Please run this script again.")
