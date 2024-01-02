import re
import tokens
import tabladesimbolos
import entradaTS

class Token:
    def __init__(self, token_type, attribute, value):
        #Inicializamos los atributos de cada token
        self.token_type = token_type
        self.attribute = attribute
        self.value = value

    def __str__(self):
        #Cada token se imprime de la siguiente manera:cd
        if self.attribute == None: #Sin atributo
            return f'< {self.token_type}, >'
        else:
            return f'< {self.token_type}, {self.attribute}>'

    def __repr__(self):
        return self.__str__()
    
    def atr(self):
        return self.attribute
    def get_type(self):
        return self.token_type

class Lexer:
    def __init__(self, tokens, source_code = None):
        #Inicializamos los atributos del lexer
        self.tokens_lenguaje = tokens
        self.source_code = source_code
        self.position = 0
        self.desplazamiento = -1
        self.token_list = []
        self.symbol_table = tabladesimbolos.tabla_de_simbolos()
        self.totalNumTablas = 1
        self.tables = []
        self.tables.append(self.symbol_table)
        self.tablaActual = 0
        self.nombreUltFuncion = ""
        self.entrada = entradaTS.entradaTS("inicio")
    
    


    def get_desplazamiento(self):
        #Devuelve el desplazamiento de la tabla de simbolos
        return self.desplazamiento
    def get_token_list(self):
        return self.token_list
    
    def get_last_token(self):
        if self.token_list:
            return self.token_list[-1]
        else:
            return None
    
    def print_symbol_table(self):
        # print(self.symbol_table)
        for tabla in self.tables:
            print(tabla)


    def analizar(self, source_code = None):
        if source_code == None :
            source_code = self.source_code
        #Analiza el código fuente y devuelve la lista de tokens
        position = 0 #Posición actual en el código fuente, es como un puntero
        while position < len(source_code): #Mientras no se haya llegado al final del código fuente
            match = None #Variable para saber si se ha encontrado un token
            for token_type, attribute, pattern in self.tokens_lenguaje: #Recorremos la lista de tokens de nuestro lenguaje
                regex = re.compile(fr'{pattern}(?![e])')
                match = regex.match(source_code, position)
                if match: #Si se ha encontrado un token
                    value = match.group(0) #Tipo de token
                    if token_type == 'entero': #Si es un entero, lo convertimos a int
                        attribute = int(value)
                    elif token_type == 'id': #Si es un identificador, lo añadimos a la tabla de simbolos
                        # comprobar si esta ya en la TS, si no esta, lo añadimos
                        if (self.symbol_table.getEntradasTS(value) == None):
                            self.symbol_table.addEntrada(value) # el lexer solo tiene que añadir los lexemas, el an. sem, añade el resto de atributos
                        attribute = 0 #Habrá que cambiarlo cuando sepamos el desplazamiento de la TS
                    elif token_type == 'cad': #Si es una cadena, el atributo es el valor de la cadena
                        attribute = value
                    self.token_list.append(Token(token_type, attribute, value)) #Añadimos el token a la lista de tokens

                    if (token_type == 'IParentesis' and (self.tablaActual != 0)):
                        self.entrada = self.symbol_table.getEntradasTS(self.nombreUltFuncion)
                        self.entrada.setTipoRetorno(self.token_list[-2].atr())

                    if (token_type == 'DParentesis' and (self.tablaActual != 0)):
                        self.tablaActual = 0



                    position = match.end() #Actualizamos la posición actual al final de la coincidencia
                    break
                
            if not match:
                #Nos aseguramos de que no sea un espacio en blanco
                if source_code[position] == ' ' or source_code[position] == '\n' or source_code[position] == '\t':
                    position += 1
                else: #Si no es un espacio en blanco, es un caracter no reconocido
                    print(f'[-] Error en la posición {position} del código fuente')
                    print(f'[-] Caracter no reconocido: "{source_code[position]}"')
                    position += 1
                    return [] #Forzamos a que devuelva una lista vacía
                
        return self.token_list


if __name__ == "__main__":
    #Archivo a analizar
    file = "casosPruebaTxt/casoPrueba1.txt"
    #Abrimos el archivo
    f = open(file, "r")
    source_code = f.read()

    #Cargamos los tokens
    tokens_leguaje = tokens.Tokens.tokens
    #Creamos el objeto mi_lexer
    mi_lexer = Lexer(tokens_leguaje, source_code)

    #Analizamos el código fuente
    tokens_analizados = mi_lexer.analizar()

    # Imprimir los tokens encontrados
    f = open("tokens.txt", "w")
    for token in tokens_analizados:
        f.write(str(token)) #Guardamos los tokens en un archivo
        f.write("\n")
    for token in tokens_analizados:
        print(token) #Imprimimos los tokens por consola

    # Imprimir la tabla de simbolos
    f = open("tablas.txt", "w")
    for tabla in mi_lexer.tables:
        f.write(str(tabla))
        f.write("\n")

    mi_lexer.print_symbol_table()