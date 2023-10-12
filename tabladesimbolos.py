import entradaTS

class tabla_de_simbolos:
    """Clase que representa una tabla de simbolos"""


    ultimo_elemento = 0

    def __init__(self, nombre):
        """Constructor de la tabla de simbolos"""
        self.symbol_table = {}
        self.nombre = nombre

    def get_desplazamiento(self):
        """Devuelve el desplazamiento del ultimo elemento de la tabla de simbolos"""
        return self.symbol_table[self.ultimo_elemento].desplazamiento
    
    def add_identifier(self, nombre, tipo, desplazamiento, numero_parametros = 0, tipo_parametros = [], modo_parametros = [], tipo_retorno = None ):
        """Añade un identificador a la tabla de simbolos"""
        self.symbol_table[nombre] = entradaTS.entradaTS(nombre, tipo, desplazamiento, tipo_retorno, numero_parametros, tipo_parametros, modo_parametros)
        self.ultimo_elemento = nombre
   
    def __str__(self) -> str:
        ret = f"Tabla de simbolos: {self.nombre}\n"
        for key in self.symbol_table:
            ret += str(self.symbol_table[key])
        return ret


# Ejemplo de uso
symbol_table = tabla_de_simbolos(1)
symbol_table.add_identifier('x', 'INTEGER', 0, 0, [], [])  # Variable
symbol_table.add_identifier('suma', 'function', 0, 2, ['INTEGER', 'INTEGER'], ['IN', 'IN'], 'INTEGER')  # Función
symbol_table.add_identifier('y', 'INTEGER', 1, 0, [], [])  # Parámetro
symbol_table.add_identifier('z', 'INTEGER', 2, 0, [], [])  # Parámetro
symbol_table.add_identifier('w', 'INTEGER', 3, 0, [], [])  # Variable
symbol_table.add_identifier('resta', 'function', 0, 2, ['INTEGER', 'INTEGER'], ['IN', 'IN'], 'INTEGER')  # Función

print(symbol_table)
print(symbol_table.get_desplazamiento())
