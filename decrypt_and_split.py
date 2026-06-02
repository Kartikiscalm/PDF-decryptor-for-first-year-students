#!/usr/bin/env python3
"""
Decrypt password-protected PDFs and split each page into 4 quadrant sub-pages.

Usage:
    1. Place encrypted PDFs in the 'Encrypted' folder
    2. Run: python3 decrypt_and_split.py
    3. Pick up the processed PDFs from the 'Unencrypted' folder
"""

import os
import copy
from pypdf import PdfReader, PdfWriter

PASSWORD = "su*phl1010n"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENCRYPTED_DIR = os.path.join(SCRIPT_DIR, "Encrypted")
UNENCRYPTED_DIR = os.path.join(SCRIPT_DIR, "Unencrypted")

# Reference image dimensions (pixels) the coordinates are based on
IMG_W, IMG_H = 1526, 1162

# Quadrant pixel boundaries: (x1, y1, x2, y2)
# Order: top-left, top-right, bottom-left, bottom-right
QUADRANTS_PX = [
    (90, 120, 720, 560),     # Slide 1 — top-left quadrant
    (780, 120, 1410, 560),   # Slide 2 — top-right quadrant
    (90, 600, 720, 1060),    # Slide 3 — bottom-left quadrant
    (780, 600, 1410, 1060),  # Slide 4 — bottom-right quadrant
]


def process_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    if reader.is_encrypted:
        reader.decrypt(PASSWORD)

    writer = PdfWriter()

    for page in reader.pages:
        mb = page.mediabox
        pdf_x0 = float(mb.left)
        pdf_y0 = float(mb.bottom)
        pdf_w = float(mb.width)
        pdf_h = float(mb.height)

        for px_x1, px_y1, px_x2, px_y2 in QUADRANTS_PX:
            new_page = copy.deepcopy(page)

            # Map pixel coordinates to PDF coordinates
            x1 = pdf_x0 + (px_x1 / IMG_W) * pdf_w
            x2 = pdf_x0 + (px_x2 / IMG_W) * pdf_w
            # Flip y-axis: pixel y goes top-down, PDF y goes bottom-up
            y1 = pdf_y0 + (1 - px_y2 / IMG_H) * pdf_h
            y2 = pdf_y0 + (1 - px_y1 / IMG_H) * pdf_h

            new_page.mediabox.lower_left = (x1, y1)
            new_page.mediabox.upper_right = (x2, y2)
            new_page.cropbox.lower_left = (x1, y1)
            new_page.cropbox.upper_right = (x2, y2)

            writer.add_page(new_page)

    with open(output_path, "wb") as f:
        writer.write(f)


def main():
    os.makedirs(ENCRYPTED_DIR, exist_ok=True)
    os.makedirs(UNENCRYPTED_DIR, exist_ok=True)

    pdf_files = [f for f in os.listdir(ENCRYPTED_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the 'Encrypted' folder.")
        print(f"Place your PDFs in: {ENCRYPTED_DIR}")
        return

    for filename in sorted(pdf_files):
        input_path = os.path.join(ENCRYPTED_DIR, filename)
        base, ext = os.path.splitext(filename)
        output_filename = f"{base}_KJ{ext}"
        output_path = os.path.join(UNENCRYPTED_DIR, output_filename)
        try:
            process_pdf(input_path, output_path)
            print(f"Done: {filename} -> {output_filename}")
        except Exception as e:
            print(f"Error: {filename} — {e}")

    print(f"\nProcessed {len(pdf_files)} file(s).")
    print(f"Output folder: {UNENCRYPTED_DIR}")


if __name__ == "__main__":
    main()
