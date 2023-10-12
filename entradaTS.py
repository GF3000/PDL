class entradaTS:
    """Clase que representa una entrada de la tabla de simbolos"""
    declarada= False

    def __init__(self, nombre, tipo = "int", desplazamiento = 0, tipo_retorno = None, numero_parametros = 0, tipo_parametros = [], modo_parametros = []):
        """Constructor de la entrada de la tabla de simbolos.
        Recibe de 1 a 7 parametros:        
        """
        self.nombre = nombre
        self.tipo = tipo
        self.desplazamiento = desplazamiento
        self.tipo_retorno = tipo_retorno
        self.numero_parametros = numero_parametros
        self.tipo_parametros = tipo_parametros
        self.modo_parametros = modo_parametros

    def __str__(self) -> str:
        ret = f"* LEXEMA: '{self.nombre}'\n"
        ret += f"+  tipo: '{self.tipo}'\n"
        if (self.tipo != "function"):
            ret += f"+ despl: {self.desplazamiento}\n"
        else: #Es funcion
            ret += f"+ numParam: {self.numero_parametros}\n"
            for i in range(len(self.tipo_parametros)):
                ret += f"+ TipoParam{i}: {self.tipo_parametros[i]}\n"
                ret += f"+ ModoParam{i}: {self.modo_parametros[i]}\n"

            ret += f"+ TipoRetorno: {self.tipo_retorno}\n"
            ret += f"+ EtiqFuncion: Et{self.nombre}\n"
        return ret

if __name__ == "__main__":
    e1 = entradaTS("x", "int", 0)
    e2 = entradaTS("suma", "funcion", 0, "int", 2, ["int", "int"], ["IN", "IN"])
    e3 = entradaTS("y", "int", 1)
    print(e1)
    print(e2)
    print(e3)