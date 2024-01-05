import re
import tokens
import tabladesimbolos
import mi_token


class Lexer:
    def __init__(self, tokens, source_code = None):
        #Inicializamos los atributos del lexer
        self.tokens_lenguaje = tokens
        self.source_code = source_code
        self.position = 0
        self.desplazamiento = -1
        self.token_list = []
        self.gestor_tabla_simbolos = tabladesimbolos.gestorTablas()
        self.totalNumTablas = 1
        self.tablaActual = 0
        self.nombreUltFuncion = ""
    
    


    def get_desplazamiento(self):
        #Devuelve el desplazamiento de la tabla de simbolos
        return self.desplazamiento
    def get_token_list(self):
        return self.token_list
    



    def analizar(self, source_code = None):
        if source_code == None :
            source_code = self.source_code
        #Analiza el código fuente y devuelve la lista de tokens
        position = 0 #Posición actual en el código fuente, es como un puntero
        while position < len(source_code): #Mientras no se haya llegado al final del código fuente
            match = None #Variable para saber si se ha encontrado un token
            for tipo, atributo, pattern in self.tokens_lenguaje: #Recorremos la lista de tokens de nuestro lenguaje
                regex = re.compile(fr'{pattern}(?![e])')
                match = regex.match(source_code, position)
                if match: #Si se ha encontrado un token
                    valor = match.group(0) #Tipo de token
                    if tipo != 'comentario': #Si es un comentario, no hacemos nada

                        if tipo == 'entero': #Si es un entero, lo convertimos a int
                            atributo = int(valor)
                        elif tipo == 'id': #Si es un identificador, lo añadimos a la tabla de simbolos
                            # comprobar si esta ya en la TS, si no esta, lo añadimos
                            if (self.gestor_tabla_simbolos.getGlobal().get(valor) == None):
                                posicion = self.gestor_tabla_simbolos.getGlobal().add(tabladesimbolos.entradaTS(valor)) # el lexer solo tiene que añadir los lexemas, el an. sem, añade el resto de atributos
                                atributo = posicion
                            else:
                                atributo = self.gestor_tabla_simbolos.getGlobal().get(valor)[1]
                        elif tipo == 'cadena': #Si es una cadena, el atributo es el valor de la cadena
                            atributo = valor


                        self.token_list.append(mi_token.Token(tipo, atributo, valor)) #Añadimos el token a la lista de tokens


                    position = match.end() #Actualizamos la posición actual al final de la coincidencia
                    break
                
            if not match:
                #Nos aseguramos de que no sea un espacio en blanco
                if source_code[position] == ' ' or source_code[position] == '\n' or source_code[position] == '\t':
                    position += 1
                else: #Si no es un espacio en blanco, es un caracter no reconocido
                    raise Exception(f'[-] Error léxico: Caracter no reconocido: \'{source_code[position]}\' en la posición {position}')
     
        self.token_list.append(mi_token.Token('EOF', None, None)) #Añadimos el token de fin de fichero
                
        return self.token_list, self.gestor_tabla_simbolos #Devolvemos la lista de tokens y la tabla de simbolos


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
    f = open("outputs/tokens.txt", "w")
    for token in tokens_analizados:
        f.write(str(token)) #Guardamos los tokens en un archivo
        f.write("\n")
    for token in tokens_analizados:
        print(token) #Imprimimos los tokens por consola

    # Imprimir la tabla de simbolos
    f = open("outputs/tablas.txt", "w")
    f.write(str(mi_lexer.gestor_tabla_simbolos))
    print(mi_lexer.gestor_tabla_simbolos)