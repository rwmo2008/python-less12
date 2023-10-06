from tkinter import *

class myFrame (Frame):
    def __init__(self):
        Frame.__init__(self)
        """Size of client window"""
        self.master.geometry("250x200")
        """Title of client window"""
        self.master.title("My GUI")
        self.grid()

        """Enter user's name"""
        self.prompt = Label(self, text = "What's your name?")
        self.prompt.grid(row = 0, column = 0)

        self.input = Entry(self)
        self.input.grid(row = 0, column = 1)

        """button; columnspan centers element"""
        #self.button_click_here = Button(self, text = "Click here",
                                   #command = self.click_here_click)
        self.button_submit = Button(self, text = "Submit",
                                    command = self.submit_click)
        #self.button_click_here.grid()
        """pady adds spacing around button"""
        self.button_submit.grid(columnspan = 2, pady = 10)

        
        """text in client window"""
        #self.message = Label(self, text = "Hello world!")
        self.my_text = StringVar()
        self.message = Label(self, textvariable = self.my_text)
        self.message.grid(columnspan = 2)

    """event: click on button -> prints message"""
    #def click_here_click(self):
        #print("You did it!")
        #self.my_text.set("You did it!")
    """event: submit text response"""
    def submit_click(self):
        output_message = "Hi " + self.input.get()
        self.my_text.set(output_message)
    
frame01 = myFrame()
frame01.mainloop()
