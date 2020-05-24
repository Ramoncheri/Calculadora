from tkinter import *
from tkinter import ttk
from cromanos import *

normal_buttons = [
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
        'W': 2   # numero de columnas de ancho
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
roman_buttons= [
    {
    "text": "=",
        "col": 0,
        "row": 5,
        "W": 4
    },
    {
        "text": "I",
        "col": 0,
        "row": 4,
    },
    {
        "text": "V",
        "col": 1,
        "row": 4,
    },
    {
        "text": "X",
        "col": 0,
        "row": 3,
    },
    {
        "text": "L",
        "col": 1,
        "row": 3,
    },
    {
        "text": "C",
        "col": 0,
        "row": 2,
    },
    {
        "text": "D",
        "col": 1,
        "row": 2,
    },
    {
        "text": "M",
        "col": 2,
        "row": 2,
        "H": 3
    },
    {
        "text": "AC",
        "col": 1,
        "row": 1,
        "W": 2
    },
    {
        "text": "/",
        "col": 3,
        "row": 1,
    },
    {
        "text": "x",
        "col": 3,
        "row": 2,
    },
    {
        "text": "-",
        "col": 3,
        "row": 3,
    },
    {
        "text": "+",
        "col": 3,
        "row": 4,
    }
]

def pinta(valor):
    print (valor)
    return valor


class Controlador(ttk.Frame):
    def __init__(self, parent):  #**kwargs son parametros definidos por pares clave- valor: ej width o height  
        ttk.Frame.__init__(self, parent, width=272, height= 300)
        self.status= 'N'
        

        self.display= Display(self)
        self.display.grid(column=0, row=0)

        self.keyboard= Keyboard(self, self.set_operation, self.status)
        self.keyboard.grid( column= 0, row= 1)

        self.selector= Selector(self.keyboard, self.change_status, self.status)
        self.selector.grid(column=0, row=1)

        self.reset(self.status)

    def reset(self, status):
        self.op1= None
        self.op2= None
        self.operation= ''
        self.signo_pulsado = False
        if self.status== 'N':
            self.dispValue= '0'
        else:
            self.dispValue= ''
        self.display.paint(self.dispValue)
        

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

    def result_total_romano(self):
        self.op2= self.n
        res= self.calculate()
        self.op1= res
        self.dispValue= res
           
    def resultParcial_romano(self, ctrButton):
        if self.op1 == None:
            self.op1 = self.n
            self.operation= ctrButton
            self.signo_pulsado = True
        elif self.op2 == None:
            self.result_total_romano()
            self.operation= ctrButton
            self.signo_pulsado = True
        elif self.signo_pulsado == False:
            self.op2= None
            self.result_total_romano()
            self.operation= ctrButton
            self.signo_pulsado= True
        elif self.signo_pulsado == True:
            if ctrButton == '+' or ctrButton =='-' or ctrButton=='x' or ctrButton== '/':
                self.op2= None
                self.operation= ctrButton
            if ctrButton== '=':
                res= self.calculate()
                self.op1= res
                self.dispValue= res


    def set_operation (self, ctrButton):
        if self.status== 'N':
            self.set_operation_N(ctrButton)
        else:
            self.set_operation_R(ctrButton)

        self.display.paint(self.dispValue)

    def set_operation_R(self, ctrButton):
        if ctrButton== 'AC':
            self.reset('R')
        
        if ctrButton == '+' or ctrButton =='-' or ctrButton=='x' or ctrButton== '/':
            self.n= RomanNumber(self.dispValue)
            if self.n.value== 'Error de formato':
                self.dispValue= self.n.value
                self.n= None
            else:
                self.resultParcial_romano(ctrButton)
                self.n= None


        if ctrButton == '=':
            
            if self.op1 != None and self.op2 == None:
                self.n=RomanNumber(self.dispValue)
                
                if self.n.value== 'Error de formato':
                    self.dispValue= self.n.value
                    self.n= None
                else:
                    self.result_total_romano()
                    self.signo_pulsado= True
                    self.n= None

            elif self.op1 !=None and self.op2 != None:
                self.n= RomanNumber(self.dispValue)
                self.resultParcial_romano(ctrButton)
                self.signo_pulsado= True

        if ctrButton in 'IVXLCDM':
            if self.dispValue== '0' or self.signo_pulsado== True:
                self.dispValue= ctrButton
                self.signo_pulsado= False
            else:
                self.dispValue += str(ctrButton)
        

    def set_operation_N(self, ctrButton):

        if ctrButton== 'C':
            self.reset('C')
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

                
            

        

    def change_status(self, status):
        self.status= status
        self.keyboard.status = status
        self.reset(self.status)

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
    
    def __init__(self, parent, command, status= 'N'):
        ttk.Frame.__init__(self, parent, width= 68, height= 50)
        self.statusSel= status
        self.__value= StringVar()  #variable de control de Tkinter
        self.__value.set(self.statusSel)  #se inicializa la variable de control
        self.command= command

        rbtn_N= ttk.Radiobutton(self, text= 'N', value= 'N', name= 'btn_N', variable= self.__value, command= self.__click)
        #rbtn_N.pack(side=TOP, fill= BOTH, expand= True)
        rbtn_N.place(x=10, y=5)
        rbtn_R= ttk.Radiobutton(self, text= 'R', value= 'R', name= 'btn_R', variable=self.__value, command= self.__click)
        #rbtn_R.pack(side=TOP, fill= BOTH, expand= True)
        rbtn_R.place(x=10, y=30)

    def __click(self):
        self.statusSel= self.__value.get()
        self.command(self.statusSel)

class Keyboard(ttk.Frame):
    def __init__(self, parent, command, status= 'N'):
        ttk.Frame.__init__(self, parent, height= 252, width= 272)
        self.__status= status
        self.listaBRomanos=[]
        self.listaBNormales= []
        self.command= command

        if self.__status== 'N':
            self.pintaNormal()
        else:
            self.pintaRomano()

        

        
    
    @property
    def status(self):  #el @property hace que se convierta en un metodo getter
        return self.__status
    
    @status.setter
    def status(self, valor):  # se convierte en un metodo setter
        self.__status= valor
        if valor== 'N':
            self.pintaNormal()
        else:
            self.pintaRomano()
    
    def pintaNormal(self):
        if len(self.listaBNormales) == 0:
            for props in normal_buttons:
                btn= CalcButton(self, props['text'],self.command, props.get('W',1), props.get('H',1))  
                self.listaBNormales.append((btn, props)) 
                btn.grid(column= props['col'], row= props['row'], columnspan=props.get('W',1), rowspan=props.get('H',1))
        else:
            for btn, props in self.listaBNormales:
                btn.grid(column= props['col'], row= props['row'], columnspan=props.get('W',1), rowspan=props.get('H',1))
 
        for borra, props in self.listaBRomanos:
            borra.grid_forget()


    def pintaRomano(self):
        if len(self.listaBRomanos)== 0:
            for props in roman_buttons:
                btn= CalcButton(self, props['text'],self.command, props.get('W',1), props.get('H',1)) 
                self.listaBRomanos.append((btn, props))  
                btn.grid(column= props['col'], row= props['row'], columnspan=props.get('W',1), rowspan=props.get('H',1))
        else:
            for btn, props in self.listaBRomanos:
                btn.grid(column= props['col'], row= props['row'], columnspan=props.get('W',1), rowspan=props.get('H',1))
        
        for borra, props in self.listaBNormales:
            borra.grid_forget()

class CalcButton(ttk.Frame):
    def __init__(self, parent, caracter, command, width=1, height=1):
        ttk.Frame.__init__(self, parent, width= 68*width, height=50*height)
        self.pack_propagate(0)

        btn= ttk.Button(self, text= caracter, command= lambda: command(caracter)) #creacion del modelo de boton. La func lambda es especifica de cada boton
        btn.pack(side= TOP, fill= BOTH, expand= True) #para que se rellene todo el frame




