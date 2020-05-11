from tkinter import ttk
from tkinter import *


class Controlador(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, width=272, height= 300)
        
class Display(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width =272, height=50)
        self.pack_propagate(1)

        lbl= ttk.Label(self, text='0', anchor= E)
        lbl.pack(side=TOP, fill= BOTH, expand= True)

            


class Selector(ttk.Radiobutton):
    pass

class CalcButton(ttk.Button):
    pass

