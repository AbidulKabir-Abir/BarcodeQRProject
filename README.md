# Barcode & QR Code Generator & Scanner

A Python GUI app to generate **Barcode (Code128)** and **QR Code** from text and scan codes from images.

## Features
- Generate Barcode (Code128)
- Generate QR Code
- Scan Barcode or QR Code from image
- Saves generated codes in `generated_codes` folder

## Requirements
- Python 3.x
- Tkinter
- python-barcode
- qrcode
- Pillow
- OpenCV
- pyzbar

---

## ** Use Cases / How to Use**
### Use Cases

1. **Generate Barcode**  
   - Enter text (example: "123456")  
   - Click **Generate Barcode**  
   - Barcode image is saved in `generated_codes` and displayed in the GUI

2. **Generate QR Code**  
   - Enter text (example: "https://example.com")  
   - Click **Generate QR Code**  
   - QR code image is saved and displayed in the GUI

3. **Scan Barcode or QR Code**  
   - Click **Scan Barcode/QR from Image**  
   - Select an image with a barcode/QR code  
   - A popup will show the detected code


## Installation
1. Clone repo:
```bash
git clone https://github.com/AbidulKabir-Abir/BarcodeQRProject.git
cd BarcodeQRProject

pip install -r requirements.txt
python main.py
### Installation
