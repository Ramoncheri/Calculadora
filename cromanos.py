class RomanNumber():

    __numRom= {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
        }

    __klist= list (__numRom.keys())

    def __init__(self, valor):
        if isinstance(valor,str):
            self.value= self.romano_a_entero(valor)
            if self.value == 'Error de formato':
                self.romanValue= self.value
            else:
                 self.romanValue= valor

        else:
            self.value= valor
            self.romanValue= self.entero_a_romano()
            if self.romanValue == 'Overflow':
                self.value = self.romanValue


    def romano_a_entero(self, rom):

        if rom== '':
            return 'Error de formato'

        entero=0
        numRepes=0
        letraAnt=''
        letra2Ant= ''
        fueResta= False
        


        for letra in rom:
            
            if letra in self.__numRom:

                if fueResta == True and self.__numRom[letra]>= self.__numRom[letra2Ant]:
                    return 'Error de formato'
                
                if letraAnt == '' or self.__numRom[letra]<= self.__numRom[letraAnt]:
                    entero += self.__numRom[letra]
                    fueResta= False
                else:
                    if self.__klist.index(letraAnt) %2 != 0:
                        return 'Error de formato'

                    if self.__klist.index(letraAnt)- self.__klist.index(letra)>2:
                        return 'Error de formato'
                            
                    else:
                        if numRepes==1 or fueResta== True:
                            return 'Error de formato'
                        else:
                            entero += self.__numRom[letra]- self.__numRom[letraAnt]*2
                            fueResta= True

            if letra not in self.__numRom:
                return 'Error de formato'
            if letra==letraAnt and numRepes==2:
                return 'Error de formato'
            elif letra==letraAnt :
                numRepes +=1           
            else:
                numRepes=0
                


            letraAnt= letra
            

        return entero


    def entero_a_romano(self): 

        if self.value> 3999 or self.value<1:
            return 'Overflow'

        componentes= self.__descomponer(self.value)

        resultado= ''
        #res = ''
        

        for valor in componentes:
            numRepes=0
            valRepes=0
            kAnt=''
            #resRepes= ''
            res = ''
            while valor>0:
                k, v= self.__busca_valor_menor_o_igual(valor)
                valor -= v
                kind= self.__klist.index(k)
                ksup= kind-1
                kinf= kind+1


                if kAnt==k:
                    
                    numRepes +=1
                    valRepes += self.__numRom[self.__klist[kind]]
                    res +=k
                    if numRepes>2:
                        
                        if valRepes + self.__numRom[self.__klist[kind]] == self.__numRom[self.__klist[ksup]]- self.__numRom[self.__klist[kind]]:
                            res= (self.__klist[kind]+ self.__klist[ksup])
                            #res = resRepes
                        #elif valRepes== 
                        # resRepes += (self.__klist[ksup]+ self.__klist[kinf])
                    
                if kAnt== '' or kAnt != k:
                    
                    if self.__klist.index(k) %2 != 0:
                        if (valor+ v) == self.__numRom[self.__klist[ksup]]- self.__numRom[self.__klist[kinf]]:
                            res = (self.__klist[kinf]+ self.__klist[ksup])
                            valor -= self.__numRom[self.__klist[ksup]]- self.__numRom[self.__klist[kinf]]
                        else:
                            res +=k
                    else:
                        res += k
                    #resultado += res
                kAnt=k
                #res = (res +resRepes)  
            resultado +=res 
        return resultado

        

    def __busca_valor_menor_o_igual(self, v):
        for key, value in self.__numRom.items():
            if value <= v:
                return key, value


    def __descomponer(self,numero):
        res =[]
        for orden in range (3,0,-1): #desde 3 a 0, restanto de 1 en 1
            resto= numero % 10**orden
            res.append(numero- resto)
            numero= resto
        res.append(numero)
        return res

    def __str__(self):
        return self.romanValue

    def __repr__(self):
        return self.romanValue

    def __add__(self, other):
        if isinstance (other, int):
            suma= self.value + other
        else:
            suma= self.value+ other.value
        resultado= RomanNumber(suma)
        return resultado

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
       
        if isinstance(other, int):
            resta= self. value - other
        else:
            resta= self.value - other.value
        resultado= RomanNumber(resta)
        return resultado

    def __rsub__(self, other):
        return self.__sub__(other)

    #def __eq__(self, other):
        #return self.value == other.value

    def __mul__(self, other):
        if isinstance(other, int):
            mult= self.value * other
        else:
            mult= self.value * other.value
        resultado= RomanNumber(mult)
        return resultado

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            divis= self.value / other
        else:
            divis= self.value / other.value
        resultado= RomanNumber(divis)
        return resultado

    def __pow__(self, other):
        if isinstance(other, int):
            potenc= self.value ** other
        else:
            potenc= self.value ** other.value
        resultado= RomanNumber(potenc)
        return resultado    
    