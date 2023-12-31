class Nodo:
    def __init__(self, tipo, valor=None, hijos=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = hijos if hijos else []

class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = {}

    def analizar(self, arbol):
        self.traversar_arbol(arbol)

    def traversar_arbol(self, nodo):
        if nodo.tipo == 'programa':
            # Iniciar análisis semántico para el programa
            pass
        elif nodo.tipo == 'declaracion_variable':
            # Realizar análisis semántico para declaraciones de variables
            self.analizar_declaracion_variable(nodo)
        elif nodo.tipo == 'asignacion':
            # Realizar análisis semántico para asignaciones
            self.analizar_asignacion(nodo)
        else:
            print(nodo.valor)
            pass

        # Recursivamente analizar nodos hijos
        for hijo in nodo.hijos:
            self.traversar_arbol(hijo)

    def analizar_declaracion_variable(self, nodo):
        # Realizar análisis semántico para declaraciones de variables
        # Actualizar la tabla de símbolos, verificar duplicados, etc.
        print(nodo.valor)   
        pass

    def analizar_asignacion(self, nodo):

        # Realizar análisis semántico para asignaciones
        # Verificar la existencia de la variable, tipos compatibles, etc.
        print(nodo.valor)
        pass

# Ejemplo de uso
arbol_sintactico = Nodo('programa', hijos=[
    Nodo('declaracion_variable', valor='x'),
    Nodo('asignacion', hijos=[
        Nodo('variable', valor='x'),
        Nodo('literal', valor=10)
    ])
])

analizador = AnalizadorSemantico()
analizador.analizar(arbol_sintactico)
