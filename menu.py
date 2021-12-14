import tkinter as tk
import buzzer_p1
import truth_or_dare

from tkinter import LEFT

LARGE_FONT = ("Verdana", 24)


class Menu(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="MENU", justify=LEFT)
        label1.pack()

        btn1 = tk.Button(self, text='Buzzer', fg="black", command=lambda: parent.show_frame(buzzer_p1.Buzzer_p1))
        btn1.pack(padx=1, pady=1)

        btn2 = tk.Button(self, text='Truth or dare?', fg="black",
                         command=lambda: parent.show_frame(truth_or_dare.Truth_or_dare))
        btn2.pack(padx=1, pady=1)
