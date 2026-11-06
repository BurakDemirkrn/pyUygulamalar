import pypdf
import gtts
import os
import tkinter as tk
from tkinter import filedialog

def pdf_metin_cikart(pdf_yolu):
    metin = ""
    pdf_okuyucu = pypdf.PdfReader(open(pdf_yolu,'rb'))
    for sayfa_num in range(len(pdf_okuyucu.pages)):
        metin += pdf_okuyucu.pages[sayfa_num].extract_text()
    return metin

def metni_sese_cevir(metin,cikti_dosyasi):
    sesli_cevirici = gtts.gTTS(text=metin,lang='tr')
    sesli_cevirici.save(cikti_dosyasi)


def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("PDF Dosyaları","*.pdf")])
    if dosya_yolu:
        pdf_metin = pdf_metin_cikart(dosya_yolu)
        metni_sese_cevir(pdf_metin,"kaydet.mp3")   
        os.system("start kaydet.mp3")

appWindow = tk.Tk()
appWindow.title("PDF Okuyucu")
appWindow.geometry("250x150")
secim_butonu = tk.Button(appWindow, text="PDF Seç",command=dosya_sec)
secim_butonu.pack(padx=20,pady=20)

appWindow.tk.mainloop()
