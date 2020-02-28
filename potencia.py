class Potencia():
    def __init__(self, cadena, potencia, tipo):
        self.caracteres = cadena
        self.letras = cadena
        self.potencia = potencia
        self.tipo = tipo
        self.contador = 0

    def alfa(self):
        while (self.potencia):
            print (self.caracteres)
        

    def verificar(self):
        if self.tipo == "-vd":
            print(self.alfa())
        elif self.tipo == "+vd":
            print(self.paso_a_paso())
    
    def paso_a_paso(self):
        pass
    
