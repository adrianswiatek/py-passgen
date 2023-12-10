from PIL import ImageTk
from qrcode import QRCode
from tkinter import Tk, Label


def show_as_qrcode(password: str) -> None:
    def qrcode_image():
        qr_code = QRCode(box_size=20, border=2)
        qr_code.add_data(password)
        return qr_code.make_image()

    def show_qrcode(image) -> None:
        tk = Tk()
        tk.title('Your generated QR Code')

        img = ImageTk.PhotoImage(image)

        label = Label(tk, image=img)
        label.pack()

        tk.mainloop()

    show_qrcode(qrcode_image())
