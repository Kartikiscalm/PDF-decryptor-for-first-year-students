# PDF Quadrant Splitter and Decryptor

A specialized tool designed to decrypt and split composite PDF pages into individual slides.

## 📖 Motivation
This project was developed in **February 2026** during my **second semester** at **IIT Jodhpur**.

The motivation came from the study materials provided for the **Electromagnetics and Optics** course. The original documents contained four slides per page, making them inconvenient for digital reading and note-taking. This project automates the process of quadrant splitting to restore a standard one-slide-per-page format.

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** installed on your machine.
- The `pypdf` library. You can install it using:
  ```bash
  pip install pypdf
  ```

### How to Use
Follow these simple steps to process your files:

1. **Prepare Folders**: Ensure you have an `Encrypted` folder in the same directory as the script.
2. **Add Files**: Place your password-protected PDF files into the `Encrypted` folder.
3. **Run the Script**: Open your terminal and run:
   ```bash
   python3 decrypt_and_split.py
   ```
4. **Collect Results**: Your processed files will appear in the `Unencrypted` folder, appended with a `_KJ` suffix (e.g., `material_KJ.pdf`).

## ⚙️ Customization

### Updating the Password
If the professor changes the password for the study materials in the future, you can easily update it:
1. Open [decrypt_and_split.py](decrypt_and_split.py) in any text editor.
2. Locate the line near the top that says `PASSWORD = "..."`.
3. Replace the text inside the quotes with the new password.
4. Save the file and run it as usual.

## 🛠 Features
- **Automatic Decryption**: Handles password-protected files seamlessly.
- **Precision Splitting**: Uses defined coordinate boundaries to split pages into four equal quadrants.
- **Batch Processing**: Handles multiple PDFs in one go.

---
*Never trust a teacher, never trust a book, trust yourself! (ifykyk)*
