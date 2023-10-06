from tkinter import *

class myFrame(Frame):
    def __init__(self):
        self.master.geometry("250x200")
        self.master.title("Text Sampler")
        self.grid()

        self.message = Label(self, text = "Some Sample Text")

        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                                      variable = self. bold_on,
                                      command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.point_size = StringVar()
        self.point_size.set("10")
        self.ten_point = Radiobutton(self, text = "10 point",
                                     variable = self.point_size,
                                     value = "10",
                                     command = self.set_font)
        self.family = StringVar()
        self.times = Radiobutton(self, text = "Times",
                                 variable = self.family, value = "times",
                                 command = self.set_font)
        self.times.grid(row = 3, column = 0)

    def set_font(self):
        new_font = "Courier 10"
        if self.bold_on.get() == 1:
            new_font = new_font + " bold"
        if self.underline_on.get() == 1:
            new_font = new_font = " underline"
        self.sample_label.config(font = new_font)
