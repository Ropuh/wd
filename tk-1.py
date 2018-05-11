import tkinter 

class Aplikacja(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

mojaAplikacja = Aplikacja()

#mojaAplikacja.geometry("400x400+400+200")
mojaAplikacja.master.title("Tytuł aplikacji")
#mojaAplikacja.master.maxsize(1000, 400)
mojaAplikacja.master.geometry("400x400")

mojaAplikacja.mainloop()
