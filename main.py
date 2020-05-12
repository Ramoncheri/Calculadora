from tkinter import *
from tkinter import ttk
import calculadora



class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Calculadora')
        self.geometry ('272x300')
        self.pack_propagate(0)

        c= calculadora.Controlador(self) #es el self de mainApp. El padre de Controlador es MainApp
        c.pack(side=TOP)#, fill=BOTH)


    def start(self):
        self.mainloop()



if __name__=='__main__':
    app= MainApp()
    app.start()



