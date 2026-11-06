from tkinter import Label, Tk
import time

appWindow = Tk()
appWindow.title("Digital Clock")
appWindow.geometry("300x200")
appWindow.resizable(0,0)
appWindow.configure(bg="Black")



text_font = ("Boulder",36,'bold')
background = "black"
foreground = "white"
border_width = 20

label = Label(appWindow,font=text_font,bg=background,fg=foreground,borderwidth=border_width)
label.grid(row=0,column=1,padx=20,pady=10)

dateLabel = Label(appWindow,font=("Boulder",18),bg=background,fg=foreground,borderwidth=border_width)
dateLabel.grid(row=1,column=1,padx=20,pady=10)

def digitalClock():
    timeLive = time.strftime("%H:%M:%S")
    label.config(text=timeLive)

    dateLive = time.strftime("%d.%m.%Y")
    dateLabel.config(text=dateLive)
    label.after(25,digitalClock)

digitalClock()





appWindow.mainloop() 