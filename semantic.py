import gramatica

class semantic:

    def analizar (gestor_TS =  None, numero_regla = None, regla_izquierda = None, pila = None, imprimir = False):
        if gestor_TS == None or numero_regla == None or regla_izquierda == None or pila == None:
            return False
        
        if imprimir:
            print("Analizando regla: ", str(numero_regla))
            print("Pila: ", pila)
            print("Regla izquierda: ", regla_izquierda)
            
        gramatica.AccionesSemanticas.get_accion(numero_regla)(gestor_TS, pila, regla_izquierda)
        
    


