import tkinter as tk
from random import randrange
from tkinter import CENTER, GROOVE, PhotoImage

import menu
import boom

LARGE_FONT = ("Verdana", 24)


class Buzzer_p2(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.count=0
        self.parent=parent
        self.value=randrange(12)
        self.img_btn1 = None
        self.img = PhotoImage(file=r"/Users/prim/PycharmProjects/pythonProject1/pep/Image_39.png")
        self.img2 = PhotoImage(file=r"/Users/prim/PycharmProjects/pythonProject1/pep/angel.png")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.img_btn1 = tk.Button(self, image=self.img,command= self.is_click11)
        self.img_btn1.grid(column = 0, row = 0)

        self.img_btn2 = tk.Button(self, image=self.img,command= self.is_click10)
        self.img_btn2.grid(column=1, row=0)

        self.img_btn3 = tk.Button(self, image=self.img,command= self.is_click9)
        self.img_btn3.grid(column=2, row=0)

        self.img_btn4 = tk.Button(self, image=self.img,command= self.is_click8)
        self.img_btn4.grid(column=0, row=1)

        self.img_btn5 = tk.Button(self, image=self.img,command= self.is_click7)
        self.img_btn5.grid(column=1, row=1)

        self.img_btn6 = tk.Button(self, image=self.img,command= self.is_click6)
        self.img_btn6.grid(column=2, row=1)

        self.img_btn7 = tk.Button(self, image=self.img,command= self.is_click5)
        self.img_btn7.grid(column=0, row=2)

        self.img_btn8 = tk.Button(self, image=self.img,command= self.is_click4)
        self.img_btn8.grid(column=1, row=2)

        self.img_btn9 = tk.Button(self, image=self.img,command= self.is_click3)
        self.img_btn9.grid(column=2, row=2)

        self.img_btn10 = tk.Button(self, image=self.img,command= self.is_click2)
        self.img_btn10.grid(column=0, row=3)

        self.img_btn11 = tk.Button(self, image=self.img,command= self.is_click1)
        self.img_btn11.grid(column=1, row=3)

        self.img_btn12 = tk.Button(self, image=self.img, command= self.is_click)
        self.img_btn12.grid(column=2, row=3)

        btn = tk.Button(self, text="Menu", fg="black", relief=GROOVE, command=lambda: parent.show_frame(menu.Menu))
        btn.grid(column=1, row=4)

    def is_click(self):
        if self.count>=self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn12["image"] = self.img2
            self.count += 1

    def is_click1(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn11["image"] = self.img2
            self.count += 1

    def is_click2(self):
        if self.count>=self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn10["image"] = self.img2
            self.count += 1

    def is_click3(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn9["image"] = self.img2
            self.count += 1

    def is_click4(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn8["image"] = self.img2
            self.count += 1

    def is_click5(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn7["image"] = self.img2
            self.count += 1

    def is_click6(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn6["image"] = self.img2
            self.count += 1

    def is_click7(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn5["image"] = self.img2
            self.count += 1

    def is_click8(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn4["image"] = self.img2
            self.count += 1

    def is_click9(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn3["image"] = self.img2
            self.count += 1

    def is_click10(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn2["image"] = self.img2
            self.count += 1

    def is_click11(self):
        if self.count >= self.value:
            self.parent.show_frame(boom.Boom)
            self.reset()
        else:
            self.img_btn1["image"] = self.img2
            self.count += 1

    def reset(self):
        self.img_btn1["image"] = self.img
        self.img_btn2["image"] = self.img
        self.img_btn3["image"] = self.img
        self.img_btn4["image"] = self.img
        self.img_btn5["image"] = self.img
        self.img_btn6["image"] = self.img
        self.img_btn7["image"] = self.img
        self.img_btn8["image"] = self.img
        self.img_btn9["image"] = self.img
        self.img_btn10["image"] = self.img
        self.img_btn11["image"] = self.img
        self.img_btn12["image"] = self.img
        self.count=0
        self.value=randrange(12)

    # def boom(self,parent):
    #     tk.Frame(self, parent)
    #
    #     img_btn1 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn1.grid()
    #
    #     img_btn2 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn2.grid()
    #
    #     img_btn3 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn3.grid()
    #
    #     img_btn4 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn4.grid()
    #
    #     img_btn5 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn5.grid()
    #
    #     img_btn6 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn6.grid()
    #
    #     img_btn7 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn7.grid()
    #
    #     img_btn8 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn8.grid()
    #
    #     img_btn9 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn9.grid()
    #
    #     img_btn10 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn10.grid()
    #
    #     img_btn11 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn11.grid()
    #
    #     img_btn12 = tk.Button(self, command=lambda: self.is_click)
    #     img_btn12.grid()





