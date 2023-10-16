class entradaTS:
    numero_entradas = 0

    def __init__(self, nombre, tipo = None, desplazamiento = 0, tipo_retorno = None, numero_parametros = 0, tipo_parametros = [], modo_parametros = []):
        self.id = entradaTS.numero_entradas
        entradaTS.numero_entradas += 1
        
        self.nombre = nombre
        self.tipo = tipo
        self.desplazamiento = desplazamiento
        self.tipo_retorno = tipo_retorno
        self.numero_parametros = numero_parametros
        self.tipo_parametros = tipo_parametros
        self.modo_parametros = modo_parametros
        # que pasa cuando es como una subtabla de una funcion y no necesita tantos parametros, dejarlo asi o crear algo especie de subentrada

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getTabla(self):
        return self.tabla

    def setTabla(self, tabla):
        self.tabla = tabla

    def getLexema(self):
        return self.lexema

    def setLexema(self, lexema):
        self.lexema = lexema

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getDesp(self):
        return self.desp

    def setDesp(self, desp):
        self.desp = desp

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

class Tipo:
    UNDEFINED = "UNDEFINED"

class Writter:
    def __init__(self, path):
        self.path = path

    def write(self, data):
        with open(self.path, "w") as file:
            file.write(data)
