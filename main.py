from tkinter import *
import qrcode
from PIL import Image, ImageTk

def generate_qr_code(data):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode.png')

    # Bild aktualisieren
    im = Image.open('qrcode.png')
    imgtk = ImageTk.PhotoImage(im)
    label_picture.config(image=imgtk)
    label_picture.image = imgtk

def on_button_click():
    data = entry_text.get()
    generate_qr_code(data)

root = Tk()
root.title('QR CODE GENERATOR 1.0')
root.geometry("700x650+710+300")
root.resizable(False, False)

btn_create = Button(text='Create', padx=20, pady=10, command=on_button_click)
btn_create.pack(anchor="ne")

# Initiales Bild
picture_1 = PhotoImage()
label_picture = Label(image=picture_1)
label_picture.pack(anchor="s")

entry_text = Entry(justify=CENTER, width=50)
entry_text.place(x=195, y=10)

root.mainloop()