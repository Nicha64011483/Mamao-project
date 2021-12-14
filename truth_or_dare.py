import tkinter as tk
from tkinter import LEFT, GROOVE, RIGHT

import menu
import truth_or_dare2

LARGE_FONT = ("Verdana", 24)


class Truth_or_dare(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        entryVar = tk.StringVar()

        label1 = tk.Label(self, text="Truth or dare?")
        label1.pack()

        label2 = tk.Label(self, text="How to play?")
        label2.pack()

        label3 = tk.Label(self,
                          text="1.Click on the bottle to spin\n 2.Wait until the bottle stop\n 3.Choose 1 person in a group to ask any questions or challenge the person who the bottle is pointing at",
                          justify=LEFT)
        label3.pack()

        btn = tk.Button(self, text="Menu", fg="black", relief=GROOVE, justify= LEFT,command=lambda: parent.show_frame(menu.Menu))
        btn.pack(padx = 1, pady = 1)

        btn2 = tk.Button(self, text="Play", fg="black", relief=GROOVE, justify = RIGHT ,
                         command=lambda: parent.show_frame(truth_or_dare2.Truth_or_dare2))
        btn2.pack(padx = 10, pady = 10)

# fixed