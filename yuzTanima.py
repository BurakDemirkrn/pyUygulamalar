import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy


def dosyaAc():
    dosyaYolu = filedialog.askopenfilename()
    if dosyaYolu:
        resim_verisi = numpy.fromfile(dosyaYolu,numpy.uint8)
        resim = cv2.imdecode(resim_verisi,cv2.IMREAD_COLOR)
        max_genislik = 1920
        max_yukseklik = 1080
        yukseklik, genislik = resim.shape[:2]
        if yukseklik > max_yukseklik or genislik > max_genislik:
            oran_genislik = max_genislik/genislik
            oran_yukseklik = max_yukseklik/yukseklik
            en_uygun_oran = min(oran_genislik,oran_yukseklik)
            yeni_genislik = int(genislik*en_uygun_oran)
            yeni_yukseklik = int(yukseklik*en_uygun_oran)
            canvas.config(width=yeni_genislik, height=yeni_yukseklik)
            resim = cv2.resize(resim,(yeni_genislik,yeni_yukseklik),interpolation=cv2.INTER_AREA)
            yuz_tanima.setInputSize((yeni_genislik,yeni_yukseklik))
        else:
            yuz_tanima.setInputSize((genislik,yukseklik))
            canvas.config(width=genislik, height=yukseklik)
            
        _, yuzler = yuz_tanima.detect(resim)
        if yuzler is not None:
            for yuz in yuzler:
                x=int(yuz[0])
                y=int(yuz[1])
                w=int(yuz[2])
                h=int(yuz[3])
                cv2.rectangle(resim, (x,y), (x+w, y+h), (255,0,255),2)
                cv2.putText(resim,"yüz",(x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

        resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)
        resim = Image.fromarray(resim)
        resim = ImageTk.PhotoImage(resim)

        canvas.img = resim
        canvas.create_image(0,0, anchor = tk.NW, image=resim)


yuz_tanima = cv2.FaceDetectorYN.create("face_detection_yunet_2026may.onnx","",(320,320),score_threshold=0.87)

root = tk.Tk()
root.title("Yüz Tanıma")
root.resizable(0,0)
canvas = tk.Canvas(root, width=600,height=400)
canvas.pack()
open_button = tk.Button(root, text="Dosya Seç",command=dosyaAc)
open_button.pack(padx=20,pady=20)
root.mainloop()


