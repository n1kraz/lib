# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 08:51:46 2026

@author: nikraz
"""

from pathlib import Path
import subprocess
import imageio_ffmpeg


# ============================================================
# SETTINGS
# ============================================================

# Folder containing the MOV files
source_folder = Path(r"C:\Users\nikraz\Desktop\Pictures from Srija")

# Folder where converted MP4 files will be saved
output_folder = source_folder / "MP4"
output_folder.mkdir(exist_ok=True)


# ============================================================
# FIND FFMPEG PROVIDED BY IMAGEIO-FFMPEG
# ============================================================

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()


# ============================================================
# FIND MOV FILES
# ============================================================

mov_files = [
    f for f in source_folder.iterdir()
    if f.is_file() and f.suffix.lower() == ".mov"
]

print()
print(f"Found {len(mov_files)} .MOV files.")
print()


# ============================================================
# CONVERT MOV → MP4
# ============================================================

for i, mov_file in enumerate(mov_files):

    output_file = output_folder / f"{mov_file.stem}.mp4"

    # Don't convert files that already exist
    if output_file.exists():
        print(f"SKIPPING (already exists): {mov_file.name}")
        continue

    print(f"Converting {i+1}: {mov_file.name} -> {output_file.name}")

    command = [
        ffmpeg,

        # Input
        "-i", str(mov_file),

        # Video: H.264
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",

        # Audio: AAC
        "-c:a", "aac",
        "-b:a", "192k",

        # Compatibility
        "-pix_fmt", "yuv420p",

        # Output
        str(output_file)
    ]

    try:
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"  ERROR converting {mov_file.name}")
        print(f"  FFmpeg error code: {e.returncode}")
        print()

print()
print("Done")
