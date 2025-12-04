import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import barcode
from barcode.writer import ImageWriter
import qrcode
import cv2
from pyzbar import pyzbar
import os

# Ensure folder exists
if not os.path.exists("generated_codes"):
    os.makedirs("generated_codes")

# GUI
root = tk.Tk()
root.title("Barcode & QR Code Generator & Scanner")
root.geometry("600x500")

def generate_barcode():
    code = entry.get()
    if not code:
        messagebox.showwarning("Input Error", "Please enter text")
        return
    CODE128 = barcode.get_barcode_class('code128')
    my_barcode = CODE128(code, writer=ImageWriter(), add_checksum=False)
    filename = f"generated_codes/{code}_barcode.png"
    my_barcode.save(filename)
    display_image(filename)

def generate_qrcode():
    code = entry.get()
    if not code:
        messagebox.showwarning("Input Error", "Please enter text")
        return
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    filename = f"generated_codes/{code}_qrcode.png"
    img.save(filename)
    display_image(filename)

def display_image(path):
    img = Image.open(path)
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk
    messagebox.showinfo("Success", f"Saved as {path}")

def scan_code():
    file_path = filedialog.askopenfilename(title="Select Image",
                                           filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"),))
    if not file_path:
        return
    img = cv2.imread(file_path)
    codes = pyzbar.decode(img)
    if not codes:
        messagebox.showinfo("Result", "No barcode or QR code detected!")
    else:
        result = "\n".join([code.data.decode("utf-8") for code in codes])
        messagebox.showinfo("Scan Result", f"Detected Code:\n{result}")

# GUI Elements
tk.Label(root, text="Enter text:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Generate Barcode", command=generate_barcode).pack(pady=5)
tk.Button(root, text="Generate QR Code", command=generate_qrcode).pack(pady=5)
tk.Button(root, text="Scan Barcode/QR from Image", command=scan_code).pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()
