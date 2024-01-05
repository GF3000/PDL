from Analizador_Sintactico import tablas

class semantic:
    def __init__(self, tabla_de_simbolos, gramatica_atributos) -> None:
        
        self.tabla_de_simbolos = tabla_de_simbolos
        self.gramatica_atributos = gramatica_atributos

    def analizar (self, parse):
        print("Analisis semantico")
        print(parse)

if __name__ == "__main__":
    tabla_de_simbolos = None
    gramatica_atributos = tablas.Reglas
    print(gramatica_atributos)
    parse = [30, 25, 23, 20, 8, 32, 25, 23, 20, 34, 49, 7, 3, 1 ]
    mi_semantico = semantic(tabla_de_simbolos, gramatica_atributos)
    mi_semantico.analizar(parse)

