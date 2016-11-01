import tkinter
import tkinter.messagebox


def main():

    gui = MyGUI()


class MyGUI:
    def __init__(self):

        self.main_window =tkinter.Tk()  # creates the main window

        self.my_button = tkinter.Button(self.main_window,\
                                        text='Click me',\
                                        command=self.do_something)

        self.quit_button = tkinter.Button(self.main_window,\
                                          text='Quit',\
                                          command=self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):

        tkinter.messagebox.showinfo('Response',\
                                    'Thanks for the click')


        # self.top_frame = tkinter.Frame(self.main_window)
        # self.bottom_frame = tkinter.Frame(self.main_window)
        #
        # self.label1 = tkinter.Label(self.top_frame, text='Hello World', fg='blue', bg='purple')
        # self.label2 = tkinter.Label(self.top_frame, text='Hello World', fg='green', bg='orange')
        # self.label3 = tkinter.Label(self.bottom_frame, text='Hello world', fg='red', bg='black')
        #
        #
        # self.label1.pack(side='top')
        # self.label2.pack(side='top')
        # self.label3.pack(side='bottom')
        #
        # self.top_frame.pack(side='top')
        # self.bottom_frame.pack(side='bottom')


        tkinter.mainloop()


main()