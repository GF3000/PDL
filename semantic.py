import tablas

class semantic:

    def analizar (gestor_TS =  None, numero_regla = None, regla_izquierda = None, pila = None, imprimir = False):
        if gestor_TS == None or numero_regla == None or regla_izquierda == None or pila == None:
            return False
        
        if imprimir:
            print("Analizando regla: ", numero_regla)
            print("Pila: ", pila)
            print("Regla izquierda: ", regla_izquierda)
            
        tablas.AccionesSemanticas.get_accion(numero_regla)(gestor_TS, pila, regla_izquierda)
        
    
        
    

if __name__ == "__main__":
    tabla_de_simbolos = None
    gramatica_atributos = tablas.Reglas.get_reglas()
    parse = [30, 25, 23, 20, 8, 32, 25, 23, 20, 34, 49, 7, 3, 1 ]
    mi_semantico = semantic(tabla_de_simbolos, gramatica_atributos)
    mi_semantico.analizar(parse)

