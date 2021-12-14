import tkinter as tk
import buzzer_p2
import menu
from tkinter import PhotoImage

LARGE_FONT = ("Verdana", 24)

class Boom(tk.Frame):

    def __init__(self,parent):
        self.parent=parent
        tk.Frame.__init__(self, parent)
        self.img = PhotoImage(file=r"/Users/prim/PycharmProjects/pythonProject1/pep/Boom-3.png")

        label = tk.Label(self, image=self.img)
        label.pack()
        label1 = tk.Label(self, text="You lose")
        label1.pack()

        btn1 = tk.Button(self, text='Restart', fg="black", command=lambda: parent.show_frame(buzzer_p2.Buzzer_p2))
        btn1.pack(padx=1, pady=1 , side = tk.LEFT)

        btn2 = tk.Button(self, text='Menu', fg="black",
                         command=lambda: parent.show_frame(menu.Menu))
        btn2.pack(padx=1, pady=1, side= tk.RIGHT)

