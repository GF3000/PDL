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
        # self.gestor_tabla_simbolos = tabladesimbolos.gestorTablas()
        self.totalNumTablas = 1
        self.tablaActual = 0
        self.nombreUltFuncion = "" 
        self.position = 0
    
    def get_linea(self):
        #Devuelve la linea actual
        return self.source_code[:self.position].count('\n') + 1

    

    def analizar(self):
        #Analiza el código fuente y devuelve la lista de tokens
        listado_tokens = []
        tokens_analizados = mi_lexer.get_token()
        listado_tokens.append(tokens_analizados)
        while tokens_analizados.tipo != 'EOF':
            tokens_analizados = mi_lexer.get_token()
            listado_tokens.append(tokens_analizados)
        return listado_tokens
        

    def get_token(self):
            source_code = self.source_code
        #Analiza el código fuente y devuelve la lista de tokens
            for tipo, atributo, pattern in self.tokens_lenguaje: #Recorremos la lista de tokens de nuestro lenguaje
                position = self.position #Posición actual en el código fuente
                if position >= len(source_code):
                    return mi_token.Token('EOF', None, None)
                else:
                    match = None #Si se ha llegado al final del código fuente, devolvemos el token de fin de fichero
                regex = re.compile(fr'{pattern}(?![e])')
                match = regex.match(source_code, position)
                if match: #Si se ha encontrado un token
                    valor = match.group(0) #Tipo de token
                    if tipo != 'comentario': #Si es un comentario, no hacemos nada

                        if tipo == 'entero': #Si es un entero, lo convertimos a int
                            atributo = int(valor)
                            if atributo > 32767 or atributo < -32768:
                                self.position = match.end()
                                raise Exception(f'[-] Error Lexico: Entero fuera de rango: \'{valor}\' en la linea {self.get_linea()}')
                            
                        elif tipo == 'cadena': #Si es una cadena, el atributo es el valor de la cadena
                            atributo = valor
                            if len(atributo) > 64:
                                self.position = match.end() #Actualizamos la posición actual al final de la coincidencia
                                raise Exception(f'[-] Error Lexico: Cadena demasiado larga: \'{valor}\' en la linea {self.get_linea()}')
                        
                        position = match.end() #Actualizamos la posición actual al final de la coincidencia
                        self.position = position
                        return(mi_token.Token(tipo, atributo, valor)) #Devolvemos el token
                    else:
                        #Si es un comeentario, pasamos el siguiente token
                        position = match.end() #Actualizamos la posición actual al final de la coincidencia
                        self.position = position
                        return self.get_token() #Añadimos el token a la lista de tokens
                else:
                    #Nos aseguramos de que no sea un espacio en blanco
                    if source_code[position] == ' ' or source_code[position] == '\n' or source_code[position] == '\t':
                        position += 1
                        self.position = position
                        return self.get_token()
                        
            
            self.position = position +1
            raise Exception(f'[-] Error Lexico: Caracter no reconocido: \'{source_code[position]}\' en la linea {self.get_linea()}')
     
                
       
if __name__ == "__main__":
    #Archivo a analizar
    file = "in.txt"
    #Abrimos el archivos
    f = open(file, "r")
    source_code = f.read()

    #Cargamos los tokens
    tokens_leguaje = tokens.Tokens.tokens
    #Creamos el objeto mi_lexer
    mi_lexer = Lexer(tokens_leguaje, source_code)


    try:
        #Analizamos el código fuente
        tokens_analizados = mi_lexer.analizar()
        #Imprimimos los tokens
        print("TOKENS")
        print("----------")
        for token in tokens_analizados:
            print(token)
        print("----------")
        print("END TOKENS")
    except Exception as e:
        print(e)
    

    