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
        "text": "/",
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
        self.reset()

        self.display= Display(self)
        self.display.grid(column=0, row=0, columnspan=4)

        self.selector= Selector(self)
        self.selector.grid(column=0, row=1)


        for props in dbuttons:
            btn= CalcButton(self, props['text'], self.set_operation, props.get('W',1), props.get('H',1))   
            btn.grid(column= props['col'], row= props['row'], columnspan=props.get('W',1), rowspan=props.get('H',1))

    def reset(self):
        self.op1= None
        self.op2= None
        self.operation= ''
        self.dispValue= '0'
        self.signo_pulsado = False
        

    def to_float(self, valor):
        return float(valor.replace(',','.'))
    def to_str(self, valor):
        return str(valor).replace('.',',')

    def calculate(self):
        if self.operation == '+':
            return self.op1+ self.op2
        elif self.operation == '-':
            return self.op1- self.op2
        elif self.operation == 'x':
            return self.op1* self.op2
        elif self.operation == '/':
            return self.op1/ self.op2
        return self.op2

    def resultParcial(self, ctrButton):
        if self.op1 == None:
            self.op1 = self.to_float(self.dispValue)
            self.operation= ctrButton
            self.signo_pulsado = True
        elif self.op2 == None:
            self.result_total()
            self.operation= ctrButton
            self.signo_pulsado = True
        elif self.signo_pulsado == False:
            self.op2= None
            self.result_total()
            self.operation= ctrButton
            self.signo_pulsado= True
        elif self.signo_pulsado == True:
            if ctrButton == '+' or ctrButton =='-' or ctrButton=='x' or ctrButton== '/':
                self.op2= None
                self.operation= ctrButton
            if ctrButton== '=':
                res= self.calculate()
                self.op1= res
                res= ('%.12g'%res)
                self.dispValue= self.to_str(res)

    def result_total(self):
        self.op2= self.to_float(self.dispValue)
        res= self.calculate()
        self.op1= res
        res= ('%.12g'%res)
        self.dispValue= self.to_str(res)
        #self.op2= ''
           

    def set_operation (self, ctrButton):

        if ctrButton== 'C':
            self.reset()
        if ctrButton== '+/-' and self.dispValue != '0':
            if self.dispValue[0] != '-':
                self.dispValue = '-' + self.dispValue
            else:
                self.dispValue = self.dispValue[1:]
        if ctrButton == ',' and ',' not in self.dispValue:
            self.dispValue += str(ctrButton)

        if ctrButton.isdigit():
            if self.dispValue== '0' or self.signo_pulsado == True:
                self.dispValue= ctrButton
                self.signo_pulsado= False
            else:
                self.dispValue += str(ctrButton)
                

        if ctrButton == '+' or ctrButton =='-' or ctrButton=='x' or ctrButton== '/':
            self.resultParcial(ctrButton)

        if ctrButton == '=':
            if self.op1 != None and self.op2 == None:
                self.result_total()
                self.signo_pulsado= True

            elif self.op1 !=None and self.op2 != None:
                #self.result_total()
                self.resultParcial(ctrButton)
                self.signo_pulsado= True

                
            

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


class Selector(ttk.Frame):
    
    def __init__(self, parent, status= 'N'):
        ttk.Frame.__init__(self, parent, width= 68, height= 50)
        self.status= status
        self.__value= StringVar()  #variable de control de Tkinter
        self.__value.set(self.status)  #se inicializa la variable de control
        
        rbtn_N= ttk.Radiobutton(self, text= 'N', value= 'N', name= 'btn_N', variable= self.__value, command= self.__click)
        #rbtn_N.pack(side=TOP, fill= BOTH, expand= True)
        rbtn_N.place(x=10, y=5)
        rbtn_R= ttk.Radiobutton(self, text= 'R', value= 'R', name= 'btn_R', variable=self.__value, command= self.__click)
        #rbtn_R.pack(side=TOP, fill= BOTH, expand= True)
        rbtn_R.place(x=10, y=30)

    def __click(self):
        self.status= self.__value.get()


class CalcButton(ttk.Frame):
    def __init__(self, parent, caracter, command, width=1, height=1):
        ttk.Frame.__init__(self, parent, width= 68*width, height=50*height)
        self.pack_propagate(0)

        btn= ttk.Button(self, text= caracter, command= lambda: command(caracter)) #creacion del modelo de boton. La func lambda es especifica de cada boton
        btn.pack(side= TOP, fill= BOTH, expand= True) #para que se rellene todo el frame




