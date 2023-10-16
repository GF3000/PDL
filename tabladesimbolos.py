import entradaTS
# clase que representa una tabla de simbolos

class tabla_de_simbolos:
    numero_tablas = 0 # llevar el cont de tablas aqui o en el gestor?

    def __init__(self, nombre):
        # self.symbol_table = {}
        self.nombre=nombre
        self.id = tabla_de_simbolos.numero_tablas
        tabla_de_simbolos.numero_tablas += 1

        self.entradasTS = {} # lista de entradas de la tabla de simbolos
        self.desplazamiento = 0

    def getID(self):
        return self.id

    def getUltimoDesp(self):
        return self.desplazamiento

    def setUltimoDesp(self, ultimo_desp):
        self.desplazamiento = ultimo_desp

# revisaaaaar cuando cree lo de entrada/subentradas
    def addEntrada(self, nombre, tipo, desplazamiento, numero_parametros = 0, tipo_parametros = [], modo_parametros = [], tipo_retorno = None ):
            self.entradasTS[nombre] = entradaTS.entradaTS(nombre, tipo, desplazamiento, tipo_retorno, numero_parametros, tipo_parametros, modo_parametros)
            self.ultimo_elemento = nombre

    def buscarTablaPorID(self, id):
        return self.entradas.get(id)

    def __str__(self):
        table_string = f"CONTENIDO DE LA TABLA # {self.id}:\n"
        for entrada in self.entradas.values():
            table_string += str(entrada) + "\n"
        return table_string
    
    # revisar como lo especifican en la pract instrucciones
    def __str__(self) -> str:
        ret = f"Tabla de simbolos: {self.id}\n"
        for entrada in self.entradasTS.values():
            ret += str(entrada) + "\n"
        return ret
    

    
# # Ejemplo de uso
# symbol_table = tabla_de_simbolos("prueba")
# symbol_table.addSubEntrada("x", "int", 0)  # Variable
# symbol_table.addEntrada('x', 'INTEGER', 0, 0, [], [])
# symbol_table.add_identifier('x', 'INTEGER', 0, 0, [], [])  # Variable
# symbol_table.add_identifier('suma', 'function', 0, 2, ['INTEGER', 'INTEGER'], ['IN', 'IN'], 'INTEGER')  # Función
# symbol_table.add_identifier('y', 'INTEGER', 1, 0, [], [])  # Parámetro
# symbol_table.add_identifier('z', 'INTEGER', 2, 0, [], [])  # Parámetro
# symbol_table.add_identifier('w', 'INTEGER', 3, 0, [], [])  # Variable
# symbol_table.add_identifier('resta', 'function', 0, 2, ['INTEGER', 'INTEGER'], ['IN', 'IN'], 'INTEGER')  # Función

# print(symbol_table)
# print(symbol_table.get_desplazamiento())