import tkinter as tk
from tkinter import LEFT, GROOVE

import menu
import buzzer_p2

LARGE_FONT = ("Verdana", 24)

class Buzzer_p1(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        entryVar = tk.StringVar()

        label1 = tk.Label(self, text = "Buzzer", justify=LEFT)
        label1.pack()

        label2 = tk.Label(self, text = "How to play?", justify=LEFT)
        label2.pack()

        label3 = tk.Label(self, text="1.Click any bottons you want\n 2.The game master will randomly choose a loser\n 3.The loser have to drink!", justify=LEFT)
        label3.pack()

        btn = tk.Button(self, text="Menu", fg="black", relief=GROOVE, command=lambda: parent.show_frame(menu.Menu))
        btn.pack()

        btn2 = tk.Button(self, text="Play", fg="black", relief=GROOVE, command=lambda: parent.show_frame(
            buzzer_p2.Buzzer_p2))
        btn2.pack()

#fixed