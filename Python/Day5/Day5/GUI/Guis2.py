import tkinter

def main():

    gui = MyGUI()

class MyGUI:
    def __init__(self):

        self.main_window =tkinter.Tk()  # creates the main window

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Hello World', fg='blue', bg='purple')
        self.label2 = tkinter.Label(self.top_frame, text='Hello World', fg='green', bg='orange')
        self.label3 = tkinter.Label(self.bottom_frame, text='Hello world', fg='red', bg='black')

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='bottom')

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')





        tkinter.mainloop()


main()

