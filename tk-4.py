import tkinter as tk
from tkinter import messagebox

def komunikat():
    zmienna = messagebox.askyesno('Pytanie','Czy napewno chcesz zamknąć program?')
    #print(zmienna)
    if zmienna == True:
        Aplikacja.destroy ()
        return

def komunikat1():
    return

Aplikacja = tk.Tk()

Aplikacja.geometry ('400x400')
Aplikacja.title ('Nazwa aplikacji')

przycisk1 = tk.Button (text='Zamknij', command=komunikat).place (x=150, y=200)
przycisk2 = tk.Button (text='Test', command=komunikat1).place (x=150, y=230)


Aplikacja.mainloop()
