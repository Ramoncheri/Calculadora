from tkinter import *
from tkinter import ttk

dbuttons = [
    {
        "text": "1",
        "col": 0,
        "row": 4
    },
    {
        "text": "2",
        "col": 1,
        "row": 4
    },
    {
        "text": "3",
        "col": 2,
        "row": 4
    },
    {
        "text": "+",
        "col": 3,
        "row": 4
    },
    {
        "text": "4",
        "col": 0,
        "row": 3
    },
    {
        "text": "5",
        "col": 1,
        "row": 3
    },
    {
        "text": "6",
        "col": 2,
        "row": 3
    },
    {
        "text": "-",
        "col": 3,
        "row": 3
    },
    {
        "text": "7",
        "col": 0,
        "row": 2
    },
    {
        "text": "8",
        "col": 1,
        "row": 2
    },
    {
        "text": "9",
        "col": 2,
        "row": 2
    },
    {
        "text": "x",
        "col": 3,
        "row": 2
    },
    {
        "text": "C",
        "col": 1,
        "row": 1
    },
    {
        "text": "+/-",
        "col": 2,
        "row": 1
    },
    {
        "text": "÷",
        "col": 3,
        "row": 1
    },
    {
        "text": "0",
        "col": 0,
        "row": 5,
        'W': 2
    },
    {
        "text": ",",
        "col": 2,
        "row": 5
    },
    {
        "text": "=",
        "col": 3,
        "row": 5
    }
]


def pinta(valor):
    print (valor)
    return valor


class Controlador(ttk.Frame):
    def __init__(self, parent):  #**kwargs son parametros definidos por pares clave- valor: ej width o height  
        ttk.Frame.__init__(self, parent, width=272, height= 300)
        self.op1= ''
        self.op2= 0
        self.operation= ''
        self.dispValue= '0'

        self.display= Display(self)
        self.display.grid(column=0, row=0, columnspan=4)

        for props in dbuttons:
            btn= CalcButton(self, props['text'], self.set_operation, props.get('W',1), props.get('H',1))   
            btn.grid(column= props['col'], row= props['row'], columnspan=props.get('W',1), rowspan=props.get('H',1))

    def to_float(self, valor):
        return float(valor.replace(',','.'))
    def to_str(self, valor):
        return valor.replace('.',',')

    def calculate(self):
        if self.operation == '+':
            return self.op1+ self.op2
        elif self.operation == '-':
            return self.op1- self.op2
        elif self.operation == '*':
            return self.op1* self.op2
        elif self.operation == '/':
            return self.op1/ self.op2
        return self.op2

    def set_operation (self, ctrButton):

        if ctrButton== 'C':
            self.dispValue= '0'
            self.op1 = ''
        if ctrButton== '+/-' and self.dispValue != '0':
            if self.dispValue[0] != '-':
                self.dispValue = '-' + self.dispValue
            else:
                self.dispValue = self.dispValue[1:]
        if ctrButton == ',' and ',' not in self.dispValue:
            self.dispValue += str(ctrButton)

        if ctrButton.isdigit():
            if self.dispValue== '0':
                self.dispValue= ctrButton
            else:
                self.dispValue += str(ctrButton)

        if ctrButton == '+':
            if self.op1 == '':
                self.op1 = self.to_float(self.dispValue)
                self.operation= ctrButton
                self.dispValue ='0'
            else:
                self.op2= self.to_float(self.dispValue)
                res= self.calculate()
                self.op1= res
                self.dispValue= '0'

        if ctrButton == '=':
            self.op2= self.to_float(self.dispValue)
            res= self.calculate()
            strRes= str(res)
            strRes= self.to_str(strRes)
            self.dispValue= strRes

        self.display.paint(self.dispValue)


class Display(ttk.Frame):
    value= '0'
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width =272, height=50)
        self.pack_propagate(0)

        s= ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 25', background= 'black', foreground= 'white')


        self.lbl= ttk.Label(self, text=self.value, anchor= E, style='my.TLabel')
        self.lbl.pack(side=TOP, fill=BOTH, expand= True)

    def paint(self, ctrButton):
        self.value= ctrButton
        self.lbl.config(text= self.value)

class Selector(ttk.Radiobutton):
    pass

class CalcButton(ttk.Frame):
    def __init__(self, parent, caracter, command, width=1, height=1):
        ttk.Frame.__init__(self, parent, width= 68*width, height=50*height)
        self.pack_propagate(0)

        btn= ttk.Button(self, text= caracter, command= lambda: command(caracter)) #creacion del modelo de boton. La func lambda es especifica de cada boton
        btn.pack(side= TOP, fill= BOTH, expand= True) #para que se rellene todo el frame




