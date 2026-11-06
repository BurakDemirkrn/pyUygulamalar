import tkinter as tk
from tkinter import filedialog
import pyqrcode 
from pyqrcode import QRCode

def qr_kod_olustur():
    url = url_girdi.get()

    if url:
        qr_url = pyqrcode.create(url)
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG Dosyaları","*.svg")])

        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=8)
            durum_etiketi.config(text="QR Kodu Oluşturuldu ve Kaydedildi")


appWindow = tk.Tk()
appWindow.title("QR Kod Oluşturucu")
etiket = tk.Label(appWindow,text="URL Girin:")
url_girdi = tk.Entry(appWindow,width=40)
qrButonu = tk.Button(appWindow,text="QR Oluştur",command=qr_kod_olustur)
durum_etiketi = tk.Label(appWindow,text="")

etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
qrButonu.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

appWindow.mainloop()