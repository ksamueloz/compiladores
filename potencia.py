class Potencia():
    def __init__(self, cadena, potencia, tipo):
        self.caracteres = cadena
        self.letras = cadena
        self.potencia = potencia
        self.tipo = tipo

    def alfa(self):
        lista = []
        for i in range(0, len(self.caracteres)):
            for j in range(0, len(self.letras)):
                lista.append(self.caracteres[i], self.letras[j])
        self.letras = lista