#Constantes
REDUCE = 0
DESPLAZA = 1
EXITO = 2
DESCRIPTORES = {REDUCE: "REDUCE", DESPLAZA: "DESPLAZA", EXITO: "EXITO"} # Para imprimir el tipo de accion

#Clase correspondiente al analizador sintactico para un analizador sintactico ascendente
class REGLA:
    """Clase correspondiente a una regla de produccion"""

    def __init__(self, izquierda, derecha):
        """Inicializa la regla de produccion. izquierda es el simbolo no terminal de la izquierda y derecha es una lista de simbolos terminales y no terminales producidos"""
        self.izquierda = izquierda
        self.derecha = derecha
    def __str__(self):
        parte_derecha = ""
        for simbolo in self.derecha:
            parte_derecha += simbolo + " "
        return self.izquierda + " -> " + parte_derecha
    
class analizador_sintactico_ascendente:
    """Clase correspondiente al analizador sintactico ascendente"""

    def __init__(self, tabla_GOTO, tabla_ACCION, reglas):
        """Inicializa el analizador sintactico con la tabla GOTO, la tabla ACCION y las reglas de produccion"""

        # Constantes
        self.REDUCE = REDUCE
        self.DESPLAZA = DESPLAZA
        self.EXITO = EXITO

        # Atributos
        self.tabla_GOTO = tabla_GOTO
        self.tabla_ACCION = tabla_ACCION
        self.reglas = reglas
        self.pila = [0]
        self.position = 0

    def GOTO(self, estado, simbolo):
        """Calcula el estado al que se llega desde el estado actual con el simbolo dado"""
        try:
            print(f"[+] Calculando GOTO({estado}, {simbolo}) -> {self.tabla_GOTO[estado][simbolo]}")
            return self.tabla_GOTO[estado][simbolo]
        except:
            print(f"[-] Calculando GOTO({estado}, {simbolo}) -> None") 
            return None

    def ACCION(self, estado, simbolo):
        """Calcula la accion a tomar y su argumento.
        Si la accion es REDUCE, el argumento es el numero de regla a aplicar.
        Si la accion es DESPLAZA, el argumento es el estado al que se llega."""

        try:
            print(f"[+] Calculando ACCION({estado}, {simbolo}) -> {DESCRIPTORES[self.tabla_ACCION[estado][simbolo][0]]}, {self.tabla_ACCION[estado][simbolo][1]}")
            return self.tabla_ACCION[estado][simbolo][0], self.tabla_ACCION[estado][simbolo][1]
        except:
            print(f"[-] Calculando ACCION({estado}, {simbolo}) -> None")
            return None, None
        
    def REGLA(self, num):
        """Devuelve la regla correspondiente al numero dado"""
        try:
            print(f"[+] Calculando REGLA({num}): {self.reglas[num]}")
            return self.reglas[num]
        except:
            print(f"[-] Calculando REGLA({num}): None")
            return None
    
    def print_estado(self):
        """Imprime el estado actual del analizador"""
        print("Pila: ", self.pila)
        print("Cadena por leer: ", self.cadena[self.position:])
       
    def analizar(self, cadena):
        """Analiza la cadena dada.
        Devuelve True si la cadena es aceptada, False en caso contrario"""
        self.cadena = cadena
        print(f"Analizando cadena: {cadena}\n")
        
        
        #Analiza la cadena de entrada y devuelve la lista de tokens
        while True:
            # Obtenemos el etsado actual
            nuevo_estado = self.pila[-1]
            # Obtenemos el token actual 
            token = self.cadena[self.position]
            # Obtenemos la accion a tomar y su argumento
            accion, argumento = self.ACCION(nuevo_estado, token)

            #Evalua la accion a tomar
            match accion:
                case self.REDUCE: 
                    # Obtenemos la regla
                    regla = self.REGLA(argumento)
                    # Eliminamos de la pila el doble de simbolos como elementos tenga la parte derecha de la regla
                    for _ in range(2*len(regla.derecha)):
                        self.pila.pop()
                    # Apilamos simbolo a la pila
                    self.pila.append(regla.izquierda)
                    # Apilamos devolucion de llamada a GOTO con estado actual y nuevo simbolo (regla.izquierda)
                    self.pila.append(self.GOTO(self.pila[-2], self.pila[-1]))

                case self.DESPLAZA:
                    # Apilamos el token a la pila
                    self.pila.append(token)
                    # Apilamos el nuevo estado a la pila
                    self.pila.append(argumento)
                    # Avanzamos en la cadena de entrada
                    self.position += 1

                case self.EXITO:
                    # Analisis sintactico correcto
                    print("[+] Cadena aceptada")
                    return True
                
                # Default
                case _: 
                    # Estado inválido
                    print("[-] Error")
                    # Imprimimos estado actual
                    self.print_estado()
                    return False
                

def nuestro_lenguaje():
    #Aqui es donde debemos rellenar las tabla
    #Podeis ver un ejemplo de como funciona con ejemplos_diapositivas

    # Tabla GOTO
    # tabla_GOTO = {ESTADO1: {NO_TERMINAL1: estado_futuro, NO_TERMINAL2: estado_futuro, ...}, ESTADO2: {...}, ESTADO3: {...}, ...}
    tabla_GOTO = {
        0: {"P": 1, "B": 2, "F": 3, "S": 4, "F1": 12, "F2": 13},
        2: {"B": 2, "F1": 12, "F2": 13},
        3: {"P" : 93, "F1" : 12, "F2" : 13, "S": 4, "B": 2, "F": 3},
        4: {"S": 2},    
        6: {"T": 46},
        9: {"E": 71, "R": 18, "U": 20, "V": 21, "D": 22, }, 
        10: {"E": 72, "R": 18, "U": 20, "V": 21, "D": 22 },
        11: {"X": 73, "E": 74, "R": 18, "U": 20, "V": 21, "D": 22 },
        16: {"E": 17, "R": 18, "U": 20, "V": 21, "D": 22 },
        19: {"U": 35, "V": 21, "D": 22 },
        24: {"U": 20, "V": 21, "D": 22 , "R": 18},
        30: {"S": 94},
        33: {"U": 3, "V": 21, "D": 22 }
    }

    # Tabla ACCION
    # Se usa un diccionario (creado con {}) para cada fila.
    # Se usaran las constantes REDUCE, DESPLAZA y EXITO en las acciones
    # tabla_ACCION = {ESTADO1: {TOKEKEN1: [accion, argumento], TOKEN2: [accion, estado_futuro], ...} , ESTADO2: {...}, ESTADO3: {...}, ...]
    tabla_ACCION = {
        0: {"function": []}

            
    }    
    # Reglas
    # Las reglas se crean con: REGLA(izquierda, [derecha])
    reglas = [

    ]

def ejemplo_diapositivas():
    # Cadena de entrada, cadena de tokens
    cadena = ["id", "+", "id", "*", "id", "+", "(", "id", "*", "id" , ")", "$"] 

    # Tabla GOTO
    tabla_GOTO = {
        0:{"E":1, "T":2, "F":3},
        4:{"E":8, "T":2, "F":3},
        6:{"T":9, "F":3},
        7:{"F":10}
    }
    # Tabla ACCION
    

    tabla_ACCION = {
        0: {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        1: {"+": [DESPLAZA, 6], "$": [EXITO, None]},
        2: {"+": [REDUCE, 2], "*": [DESPLAZA, 7], ")": [REDUCE, 2], "$": [REDUCE, 2]},
        3: {"+": [REDUCE, 4], "*": [REDUCE, 4], ")": [REDUCE, 4], "$": [REDUCE, 4]},
        4: {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        5: {"+": [REDUCE, 6], "*": [REDUCE, 6], ")": [REDUCE, 6], "$": [REDUCE, 6]},
        6: {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        7: {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        8: {"+": [DESPLAZA, 6], ")": [DESPLAZA, 11]},
        9: {"+": [REDUCE, 1], "*": [DESPLAZA, 7], ")": [REDUCE, 1], "$": [REDUCE, 1]},
        10: {"+": [REDUCE, 3], "*": [REDUCE, 3], ")": [REDUCE, 3], "$": [REDUCE, 3]},
        11: {"+": [REDUCE, 5], "*": [REDUCE, 5], ")": [REDUCE, 5], "$": [REDUCE, 5]}
    }

    # Reglas
    reglas = [
        REGLA("E", ["E"]),
        REGLA("E", ["E", "+", "T"]),
        REGLA("E", ["T"]),
        REGLA("T", ["T", "*", "F"]),
        REGLA("T", ["F"]),
        REGLA("F", ["(", "E", ")"]),
        REGLA("F", ["id"])
    ]

    # Creamos el analizador sintactico
    analizador = analizador_sintactico_ascendente(tabla_GOTO, tabla_ACCION, reglas)
    # Lo ejecutamos
    analizador.analizar(cadena)

if __name__ == "__main__":
    ejemplo_diapositivas()