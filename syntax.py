
REDUCE = 0
DESPLAZA = 1
EXITO = 2

#Clase correspondiente al analizador sintactico para un analizador sintactico ascendente
class REGLA:
    izquierda = ""
    derecha = []
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha
    def __str__(self):
        return self.izquierda + " -> " + str(self.derecha)
    
class analizador_sintactico_ascendente:
    #CONSTANTES:
    REDUCE = 0
    DESPLAZA = 1
    EXITO = 2

    #ATRIBUTOS:
    cadena = ""
    pila = [0]
    tabla_GOTO = []
    tabla_ACCION = []
    reglas = []
    simbolos_no_terminales = []
    position = 0

    def __init__(self, cadena, tabla_GOTO, tabla_ACCION, reglas):
        self.cadena = cadena
        self.tabla_GOTO = tabla_GOTO
        self.tabla_ACCION = tabla_ACCION
        self.reglas = reglas
        self.pila = [0]
        for regla in reglas:
            if regla.izquierda not in self.simbolos_no_terminales:
                self.simbolos_no_terminales.append(regla.izquierda)

    def GOTO(self, estado, simbolo):
        try:
            print(f"[+] Calculando GOTO({estado}, {simbolo}) -> {self.tabla_GOTO[estado][simbolo]}")
            return self.tabla_GOTO[estado][simbolo]
        except:
            print(f"[-] Calculando GOTO({estado}, {simbolo}) -> None") 
            return None, None

    def ACCION(self, estado, simbolo):
        try:
            print(f"[+] Calculando ACCION({estado}, {simbolo}) -> {self.tabla_ACCION[estado][simbolo]}")
            return self.tabla_ACCION[estado][simbolo][0], self.tabla_ACCION[estado][simbolo][1]
        except:
            print(f"[-] Calculando ACCION({estado}, {simbolo}) -> None")
            return None, None
        
    def REGLA(self, num):
        try:
            print(f"[+] Calculando REGLA({num}) -> {self.reglas[num]}")
            return self.reglas[num]
        except:
            print(f"[-] Calculando REGLA({num}) -> None")
            return None
    def print_estado(self):
        print("Pila: ", self.pila)
        print("Cadena por leer: ", self.cadena[self.position:])
       
    
    def analizar(self):
        #Analiza la cadena de entrada y devuelve la lista de tokens
        while True:
            elemento = self.pila[-1]
            
            if (elemento in self.simbolos_no_terminales): #En la cima de la pila hay un simbolo
                self.pila.append(self.GOTO(self.pila[-2], elemento))

            else:  #En la cima de la pila hay un estado    
                token = self.cadena[self.position]
                accion, argumento = self.ACCION(elemento, token)
                match accion:
                    case self.REDUCE: 
                        regla = self.REGLA(argumento)
                        for _ in range(2*len(regla.derecha)):
                            self.pila.pop()
                        self.pila.append(regla.izquierda)

                    case self.DESPLAZA:
                        self.pila.append(token)
                        self.pila.append(argumento)
                        self.position += 1

                    case self.EXITO:
                        print("[+] Cadena aceptada")
                        return True
                    case _:
                        print("[-] Error")
                        self.print_estado()
                        return False
                

def nuestro_lenguaje():
    #Aqui es donde debemos rellenar las tabla
    #Podeis ver un ejemplo de como funciona con ejemplos_diapositivas

    # Tabla GOTO
    # tabla_GOTO = {ESTADO1: {NO_TERMINAL1: estado_futuro, NO_TERMINAL2: estado_futuro, ...}, ESTADO2: {...}, ESTADO3: {...}, ...}
    tabla_GOTO = {
        
    }

    # Tabla ACCION
    # Se usa un diccionario (creado con {}) para cada fila.
    # Se usaran las constantes REDUCE, DESPLAZA y EXITO en las acciones
    # tabla_ACCION = [{TOKEKEN1: [accion, argumento], TOKEN2: [accion, estado_futuro], ...} , {...}, {...}, ...]
    tabla_ACCION = [
            
    ]
    
    # Reglas
    # Las reglas se crean con: REGLA(izquierda, [derecha])
    reglas = [

    ]

def ejemplo_diapositivas():
    # Cadena de entrada, cadena de tokens
    cadena = ["id", "+", "id", "*", "id", "$"] 

    # Tabla GOTO
    tabla_GOTO = {
        0:{"E":1, "T":2, "F":3},
        4:{"E":8, "T":2, "F":3},
        6:{"T":9, "F":3},
        7:{"F":10}
    }
    # Tabla ACCION
    

    tabla_ACCION = [
        {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        {"+": [DESPLAZA, 6], "$": [EXITO, None]},
        {"+": [REDUCE, 2], "*": [DESPLAZA, 7], ")": [REDUCE, 2], "$": [REDUCE, 2]},
        {"+": [REDUCE, 4], "*": [REDUCE, 4], ")": [REDUCE, 4], "$": [REDUCE, 4]},
        {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        {"+": [REDUCE, 6], "*": [REDUCE, 6], ")": [REDUCE, 6], "$": [REDUCE, 6]},
        {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        {"id": [DESPLAZA, 5], "(": [DESPLAZA, 4]},
        {"+": [DESPLAZA, 6], ")": [DESPLAZA, 11]},
        {"+": [REDUCE, 1], "*": [DESPLAZA, 7], ")": [REDUCE, 1], "$": [REDUCE, 1]},
        {"+": [REDUCE, 3], "*": [REDUCE, 3], ")": [REDUCE, 3], "$": [REDUCE, 3]},
        {"+": [REDUCE, 5], "*": [REDUCE, 5], ")": [REDUCE, 5], "$": [REDUCE, 5]}
    ]

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
    analizador = analizador_sintactico_ascendente(cadena, tabla_GOTO, tabla_ACCION, reglas)
    # Lo ejecutamos
    analizador.analizar()

if __name__ == "__main__":
    ejemplo_diapositivas()