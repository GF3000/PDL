import re
import tokens

class Token:
    def __init__(self, token_type, attribute, value):
        #Inicializamos los atributos de cada token
        self.token_type = token_type
        self.attribute = attribute
        self.value = value

    def __str__(self):
        #Cada token se imprime de la siguiente manera:
        if self.attribute == None: #Sin atributo
            return f'< {self.token_type}, >'
        else:#Con atributo
            return f'< {self.token_type}, {self.attribute}>'

    def __repr__(self):
        return self.__str__()

class Lexer:
    def __init__(self, tokens, source_code):
        #Inicializamos los atributos del lexer
        self.tokens_lenguaje = tokens
        self.source_code = source_code
        self.position = 0
        self.desplazamiento = 0
        self.token_list = []
    def get_desplazamiento(self):
        #Devuelve el desplazamiento de la tabla de simbolos, FALTA IMPLEMENTAR
        return self.desplazamiento
    def get_token_list(self):
        #Devuelve la lista de tokens
        return self.token_list
    def analizar(self):
        #Analiza el código fuente y devuelve la lista de tokens
        position = 0 #Posición actual en el código fuente, es como un puntero
        while position < len(source_code): #Mientras no se haya llegado al final del código fuente
            match = None #Variable para saber si se ha encontrado un token
            for token_type, attribute, pattern in tokens_leguaje: #Recorremos la lista de tokens de nuestro lenguaje
                regex = re.compile(pattern)
                match = regex.match(source_code, position)
                if match: #Si se ha encontrado un token
                    value = match.group(0) #Tipo de token
                    if token_type == 'INTEGER': #Si es un entero, lo convertimos a int
                        attribute = int(value)
                    elif token_type == 'IDENTIFIER': #Si es un identificador, lo añadimos a la tabla de simbolos, FALTA IMPLEMENTAR
                        attribute = self.desplazamiento
                        self.desplazamiento += 1 #Hay que cambiarlo por el desplazamiento de la tabla de simbolos
                    elif token_type == 'CAD': #Si es una cadena, el atributo es el valor de la cadena 
                        attribute = value
                    self.token_list.append(Token(token_type, attribute, value)) #Añadimos el token a la lista de tokens
                    position = match.end() #Actualizamos la posición actual al final de la coincidencia
                    break
                

            if not match: #Si no se ha encontrado un token
                #Nos aseguramos de que no sea un espacio en blanco
                if source_code[position] == ' ' or source_code[position] == '\n' or source_code[position] == '\t':
                    position += 1
                else:#Si no es un espacio en blanco, es un caracter no reconocido
                    print(f'[-] Error en la posición {position} del código fuente')
                    print(f'[-] Caracter no reconocido: "{source_code[position]}"')
                    position += 1
                    return [] #Forzamos a que devuelva una lista vacía
                
        return self.token_list



#Archivo a analizar
file = "in4.txt"
#Abrimos el archivo
f = open(file, "r")
source_code = f.read()

#Cargamos los tokens
tokens_leguaje = tokens.Tokens.tokens
#Creamos el objeto mi_lexer
mi_lexer = Lexer(tokens_leguaje, source_code)

#Analizamos el código fuente
tokens_analizados = mi_lexer.analizar()


f = open("tokens.txt", "w")
for token in tokens_analizados:
    f.write(str(token)) #Guardamos los tokens en un archivo
    f.write("\n")
    print(token) #Imprimimos los tokens por consola

