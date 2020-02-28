class Potencia():
    def __init__(self, cadena, potencia, tipo):
        self.caracteres = cadena
        self.letras = cadena
        self.potencia = potencia
        self.tipo = tipo
        self.contador = 0

    def alfa(self):
        lista = []
        for i in range(0, len(self.caracteres)):
            for j in range(0, len(self.letras)):
                self.contador += self.contador
                if(self.potencia == self.contador):
                    print(self.caracteres+self.letras)
                else:
                    print(self.caracteres+self.letras)            