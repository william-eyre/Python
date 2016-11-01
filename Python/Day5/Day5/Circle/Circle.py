import tkinter
import math


class CircleArea(tkinter.Frame):
    def __init__(self):
        # Sets up the window and widgets.
        # self.main_window = tkinter.Tk ( )
        tkinter.Frame.__init__(self)
        self.master.title("Circle Area")
        self.grid()
        # Label and field for the radius
        self._radiusLabel = tkinter.Label(self, text="Radius")
        self._radiusLabel.grid(row=0, column=0)
        self._radiusVar = tkinter.DoubleVar()
        self._radiusEntry = tkinter.Entry(self, textvariable=self._radiusVar)
        self._radiusEntry.grid(row=0, column=1)
        #  Label and field for the area
        self._areaLabel = tkinter.Label(self, text="Area")
        self._areaLabel.grid(row=1, column=0)
        self._areaVar = tkinter.DoubleVar()
        self._areaEntry = tkinter.Entry(self, textvariable=self._areaVar)
        self._areaEntry.grid(row=1, column=1)
        # compute results
        self._computeLabel = tkinter.Label(self, text="Result")
        # self._areaLabel.grid ( row=2, column=0 )
        self._computeLabel.grid(row=2, column=0)
        self._computeVar = tkinter.DoubleVar()
        self._computeLabel = tkinter.Entry(self, textvariable=self._computeVar)
        self._computeLabel.grid(row=2, column=1)
        # The command button
        self._button = tkinter.Button(self, text="Compute", command=self._area)
        self._button.grid(row=3, column=0, columnspan=2)

    def _area(self):
        # Event handler for the button.
        radius = self._radiusVar.get()
        area = radius ** 2 * math.pi
        self._computeVar.set(format(area, ',.2f'))


def main():
    CircleArea().mainloop()


main()
