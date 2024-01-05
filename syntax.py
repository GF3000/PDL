# from Analizador_Sintactico import tablas
import tablas
import mi_token
import semantic

#Constantes
REDUCE = tablas.Constantes.REDUCE
DESPLAZA = tablas.Constantes.DESPLAZA
EXITO = tablas.Constantes.EXITO
DESCRIPTORES = tablas.Constantes.DESCRIPTORES
FILE = "outputs/parse.txt"


class Syntax:
    """Clase correspondiente al analizador sintactico ascendente"""

    def __init__(self, tabla_GOTO, tabla_ACCION, reglas, gestor_TS = None,  imprimir = False):
        """Inicializa el analizador sintactico con la tabla GOTO, la tabla ACCION y las reglas de produccion. El parametro impresion indica si se imprimen los pasos del analisis sintactico"""

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
        self.cadena = ""
        self.imprimir = imprimir
        self.gestor_TS = gestor_TS

    def GOTO(self, estado, simbolo):
        """Calcula el estado al que se llega desde el estado actual con el simbolo dado"""
        try:
            if self.imprimir:
                print(f"[+] Calculando GOTO({estado}, {simbolo}) -> {self.tabla_GOTO[estado][simbolo]}")
            return self.tabla_GOTO[estado][simbolo]
        except:
            if self.imprimir:
                print(f"[-] Calculando GOTO({estado}, {simbolo}) -> None") 
            return None

    def ACCION(self, estado, simbolo):
        """Calcula la accion a tomar y su argumento.
        Si la accion es REDUCE, el argumento es el numero de regla a aplicar.
        Si la accion es DESPLAZA, el argumento es el estado al que se llega."""

        try:
            if self.imprimir:
                print(f"[+] Calculando ACCION({estado}, {simbolo}) -> {DESCRIPTORES[self.tabla_ACCION[estado][simbolo][0]]}, {self.tabla_ACCION[estado][simbolo][1]}")
            return self.tabla_ACCION[estado][simbolo][0], self.tabla_ACCION[estado][simbolo][1]
        except:
            if self.imprimir:
                print(f"[-] Calculando ACCION({estado}, {simbolo}) -> None")
            return None, None
        
    def REGLA(self, num):
        """Devuelve la regla correspondiente al numero dado"""
        try:
            if self.imprimir:
                print(f"[+] Calculando REGLA({num}): {self.reglas[num]}")
            return self.reglas[num]
        except:
            if self.imprimir:
                print(f"[-] Calculando REGLA({num}): None")
            return None
    
    def print_estado(self):
        """Imprime el estado actual del analizador"""
        print("Pila: ", self.pila)
        print("Cadena por leer: ", self.cadena[self.position:])
       
    def analizar(self, listado_tokens):
        """Analiza la cadena dada.
        Devuelve True si la cadena es aceptada, False en caso contrario"""
        self.cadena = listado_tokens
        self.pila = [0]
        self.position = 0
        # print(f"\nAnalizando cadena: {cadena}\n")
        texto_archivo = "ascendente "
        
        
        #Analiza la cadena de entrada y devuelve la lista de tokens
        while self.position < len(self.cadena):
            # Obtenemos el etsado actual
            nuevo_estado = self.pila[-1]
            if isinstance(nuevo_estado, mi_token.Token):
                nuevo_estado = nuevo_estado.tipo
            if isinstance(nuevo_estado, mi_token.Estado):
                nuevo_estado = nuevo_estado.estado
            # Obtemso el token actual
            token = self.cadena[self.position]
            # Obtenemos la accion a tomar y su argumento
            accion, argumento = self.ACCION(nuevo_estado, token.tipo)

            #Evalua la accion a tomar
            match accion:
                case self.REDUCE: 
                    # Obtenemos la regla
                    regla = self.REGLA(argumento)
                    texto_archivo += str(argumento) + " "
                    # Eliminamos de la pila el doble de simbolos como elementos tenga la parte derecha de la regla
                    # print("Pila pre-reduccion: ", self.pila)
                    regla_izquierda = mi_token.Estado(estado = regla.izquierda)
                    try:
                        semantic.semantic.analizar(gestor_TS=self.gestor_TS, numero_regla=argumento, regla_izquierda= regla_izquierda, pila = self.pila, imprimir = self.imprimir)
                    except Exception as e:
                        raise(e)

                    for _ in range(2*len(regla.derecha)):
                        self.pila.pop()
                    # Apilamos simbolo a la pila
                    self.pila.append(regla_izquierda)
                    # print("Pila post-reduccion: ", self.pila)
                    # Apilamos devolucion de llamada a GOTO con estado actual y nuevo simbolo (regla.izquierda)
                    self.pila.append(self.GOTO(self.pila[-2], regla_izquierda.estado))
                    # if nulo == None: self.pila.append(self.GOTO(self.pila[-4], self.pila[-1]))

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
                    with open(FILE, "w") as f:
                        f.write(texto_archivo + "\n")
                    return True
                
                # Default
                case _: 
                    # Estado inválido
                    # Imprimimos estado actual
                    if self.imprimir:
                        self.print_estado()
                    with open(FILE, "w") as f:
                       f.write(texto_archivo + "\n")
                    raise Exception(f"[-] Error en la posición {self.position} de la cadena de entrada. Token erroneo: {self.cadena[self.position]}")
        if self.imprimir:
            self.print_estado()
            raise(Exception("[-] Error desconocido"))
   
                

def nuestro_lenguaje(cadena):
    #Aqui es donde debemos rellenar las tabla
    #Podeis ver un ejemplo de como funciona con ejemplos_diapositivas

    # Tabla GOTO
    # tabla_GOTO = {ESTADO1: {NO_TERMINAL1: estado_futuro, NO_TERMINAL2: estado_futuro, ...}, ESTADO2: {...}, ESTADO3: {...}, ...}
    tabla_GOTO = tablas.Tabla_GOTO.get_tabla_GOTO()
    tabla_ACCION = tablas.Tabla_ACCION.get_tabla_ACCION()
    reglas = tablas.Reglas.get_reglas()
    mi_analizador = Syntax(tabla_GOTO, tabla_ACCION, reglas)
    return mi_analizador.analizar(cadena)

if __name__ == "__main__":


    # Cadenas con las que no funciona
    # lista_tokens = [
    # ["if", "(", "id", "+", "id", ")", "return", "true", ";", "$"]
    # ,["if", "(", "id", "<", "id", ")", "return", "true", ";", "$"]
    # ,["id", "=", "id", "+", "id", ";", "if", "(", "!", "id", ")", "return", "id", ";", "$"] 
    # ,["id", "=", "id", "+", "id", "+", "id","+", "id", ";", "$"] 
    # ,["id", "=", "id", "<", "id", ";", "$"] 
    # ,["let", "int", "id", ";", "if", "(", "!", "id", ")", "return", "id", "+", "id", ";", "$"]
    # ,["if", "(", "true", ")", "return", "true", ";", "$"]
    # ,["function", "id", "void", "(","int" ,"id", ")", "{", "}", "$"] # el estado 13 estaba mal hecho en el excel
    # ,["get","id", ";","get","id", ";", "put","id", ";", "$"]
    # ,["get","id", ";","get","id", ";","id","=","id", ";","put","id", ";", "$"]
    # ,["id","=", "!", "id", ";", "$"]

    # ,["let", "int", "id", ";","let", "string", "id", ";", "let", "boolean", "id", ";", "$"]
    # ,["let", "int", "id", ";", "$"]
    # ,["let", "int", "id", ";","let", "string", "id", ";", "let", "boolean", "id", ";", "id", "=", "id", ";", "$"], # le faltaba ; al final
    # ["for", "(", "id", "=", "entero", ";", "true", ";", "--", "id", ")", "{", "}", "$"]
    # ]

    lista_tokens = [
        ['for', 'parentesisabierto', 'id', 'asignacion', 'entero', 'puntoycoma', 'id', 'menor', 'entero', 'puntoycoma', 'id', 'asignacion', 'id', 'suma', 'entero', 'parentesiscerrado', 'llaaveabierta', 'llavecerrada', 'EOF']
    ]
    
    cadenas_que_no_funcionan = []
    cadenas_que_funcionan = []
    mi_syntax = Syntax(tablas.Tabla_GOTO.get_tabla_GOTO(), tablas.Tabla_ACCION.get_tabla_ACCION(), tablas.Reglas.get_reglas())
    for tokens in lista_tokens:

        if(mi_syntax.analizar(tokens)):
            cadenas_que_funcionan.append(tokens)
        else:
            cadenas_que_no_funcionan.append(tokens)

    print("Cadenas que funcionan: ")
    for cadena in cadenas_que_funcionan:
        print(cadena)
    print("Cadenas que no funcionan: ")
    for cadena in cadenas_que_no_funcionan:
        print(cadena)

    # print("Imprimiendo trazas de cadenas que no funcionan: ")
    # for cadena in cadenas_que_no_funcionan:
    #     nuestro_lenguaje(cadena)
   


