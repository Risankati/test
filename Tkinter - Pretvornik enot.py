# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

window = Tkinter.Tk()
window.title("Pretvornik Km v M")
window.geometry("400x400")

#pozdrav
pozdrav = Tkinter.Label(window, text="Pozdravljeni! Sem program, ki pretvarja kilometre v milje.")
pozdrav.pack()

napis = Tkinter.Label(window, text="V spodnje polje vnesi število kilometrov, ki jih želiš pretvoriti v milje.")
napis.pack()

#vnos
vnos = Tkinter.Entry(window)
vnos.pack()

#what
def pretvori():
    mi = int(vnos.get()) * 0.621371

#what
def rezultat():
    "{0} KM = {1} MI.".format(km, mi)

#what
tkMessageBox.showinfo(rezultat)

#gumb
gumb = Tkinter.Button(window, text = "Pretvori", command="pretvori")
gumb.pack()
window.mainloop()
