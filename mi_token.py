class Token:
    def __init__(self, token_type, attribute, value):
        #Inicializamos los atributos de cada token
        self.tipo = token_type
        self.atributo = attribute
        self.valor = value

    def __str__(self):
        #Cada token se imprime de la siguiente manera:cd
        if self.atributo == None: #Sin atributo
            return f'< {self.tipo}, >'
        else:
            return f'< {self.tipo}, {self.atributo} >'

    def __repr__(self):
        return self.__str__()
    
    def atr(self):
        return self.atributo
    def get_type(self):
        return self.tipo

class Estado:
    def __init__(self, estado = None, tipo = None):
        self.estado = estado
        self.tipo = tipo

    def __str__(self):
        return f'< {self.estado}, {self.tipo} >'

    def __repr__(self):
        return self.__str__()