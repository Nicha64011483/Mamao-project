import tkinter as tk
from tkinter import LEFT, GROOVE

import menu

LARGE_FONT = ("Verdana", 24)


class Truth_or_dare2(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        entryVar = tk.StringVar()

        label1 = tk.Label(self, text="truth or dare?", justify=LEFT)
        label1.pack()

        btn = tk.Button(self, text="Menu", fg="black", relief=GROOVE, command=lambda: parent.show_frame(menu.Menu))
        btn.pack(side = LEFT,padx = 5)

# fixed