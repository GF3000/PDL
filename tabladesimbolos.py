import entradaTS
# clase que representa una tabla de simbolos

class tabla_de_simbolos:
    numero_tablas = 0

    def __init__(self):
        self.id = tabla_de_simbolos.numero_tablas
        tabla_de_simbolos.numero_tablas += 1

        self.entradasTS = {} # lista de entradas de la tabla de simbolos
        self.desplazamiento = -1

    def getID(self):
        return self.id

    def getUltimoDesp(self):
        return self.desplazamiento

    def setUltimoDesp(self, ultimo_desp):
        self.desplazamiento = ultimo_desp

    def addEntrada(self, nombre, tipo = None, desplazamiento = 0, numero_parametros = 0, tipo_parametros = [], modo_parametros = [], tipo_retorno = None ):
            self.entradasTS[nombre] = entradaTS.entradaTS(nombre, tipo, desplazamiento, tipo_retorno, numero_parametros, tipo_parametros, modo_parametros)
            self.ultimo_elemento = nombre
    
    def getEntradasTS(self, nombre):
        for entrada in self.entradasTS.values():
            if entrada.nombre == nombre:
                return entrada  
        return None 

    def buscarTablaPorID(self, id):
        return self.entradas.get(id)

    # revisar como lo especifican en la pract instrucciones
    def __str__(self) -> str:
        ret = f"Tabla #{self.id}:\n"
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