# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:08:49 2026

@author: nikraz
"""

from pathlib import Path
from PIL import Image
import pillow_heif

# Enable HEIC/HEIF support in Pillow
pillow_heif.register_heif_opener()

# Folder containing the images
source_folder = Path(r"C:\Users\nikraz\Desktop\Pictures from Srija")

# Create nested output folder
output_folder = source_folder / "JPEG"
output_folder.mkdir(exist_ok=True)

# Find all HEIC files, regardless of capitalization
heic_files = [
    f for f in source_folder.iterdir()
    if f.is_file() and f.suffix.lower() == ".heic"
]

print()
print(f"Found {len(heic_files)} .HEIC images.")
print()

for i, heic_file in enumerate(heic_files):
    output_file = output_folder / f"{heic_file.stem}.jpeg"

    try:
        with Image.open(heic_file) as image:
            image = image.convert("RGB")
            image.save(output_file, "JPEG", quality=95)

        print(f"Converting {i+1}: {heic_file.name} -> JPEG/{output_file.name}")

    except Exception as e:
        print(f"ERROR: {heic_file.name}: {e}")

print("\nDone.")