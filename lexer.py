import re
import tokens
import tabladesimbolos

class Token:
    def __init__(self, token_type, attribute, value):
        self.token_type = token_type
        self.attribute = attribute
        self.value = value

    def __str__(self):
        if self.attribute == None:
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
    def __init__(self, tokens, source_code):
        self.tokens_lenguaje = tokens
        self.source_code = source_code
        self.position = 0
        self.desplazamiento = 0
        self.token_list = []
        self.symbol_table = tabladesimbolos.tabla_de_simbolos("principal")

    def get_desplazamiento(self):
        return self.desplazamiento
    def get_token_list(self):
        return self.token_list
    
    def get_last_token(self):
        if self.token_list:
            return self.token_list[-1]
        else:
            return None
    
    def print_symbol_table(self):
        print(self.symbol_table)


    def analizar(self):
        position = 0
        while position < len(source_code):
            match = None
            for token_type, attribute, pattern in tokens_leguaje:
                regex = re.compile(pattern)
                match = regex.match(source_code, position)
                if match:
                    value = match.group(0)
                    if token_type == 'INTEGER':
                        attribute = int(value)
                    elif token_type == 'IDENTIFIER':

                        token_atrib = self.get_last_token().atr()
                        # hacer una funcion de si esta el id en la tabla porque a veces no tiene la palres delante
                        # p. ej: tienes int x; o puedes tener x=0 a secas y deberia meter a la tabla la x
                        if self.get_last_token().get_type() == 'PalRes':
                            if token_atrib == 'function':
                                # --- cosas por hacer
                                # creo una tabla para la funcion
                                # meterlas en un array o algo del lexer o gestor para guardarlas
                                # igualmente, tiene que estar tbn en la tabla principal lo que meta ahi
                                self.symbol_table.addEntrada(value, self.get_last_token().atr(), 0, 0, [], []) # esta mal, hay que calcular lo de parametros y desplazamiento

                            self.symbol_table.addEntrada(value, self.get_last_token().atr(), 0, 0, [], [])
                            if token_atrib == 'INTEGER':
                                self.desplazamiento += 1 # revisar si estoy haciendo el desplazamiento bn, 2B?
                            elif token_atrib == 'STRING':
                                self.desplazamiento += len(value)
                            elif token_atrib == 'BOOLEAN':
                                self.desplazamiento += 1
                            self.symbol_table.setUltimoDesp(self.desplazamiento)
                            # no esta actualizando el desplazamiento -- revisar

                    elif token_type == 'CAD':
                        attribute = value
                    self.token_list.append(Token(token_type, attribute, value))
                    position = match.end()
                    break
                
            if not match:
                #Nos aseguramos de que no sea un espacio en blanco
                if source_code[position] == ' ' or source_code[position] == '\n' or source_code[position] == '\t':
                    position += 1
                else:
                    print(f'[-] Error en la posición {position} del código fuente')
                    print(f'[-] Caracter no reconocido: "{source_code[position]}"')
                    position += 1
                    return []
                
        return self.token_list




# Definición de tokens y sus expresiones regulares

# Ejemplo de código fuente
#source_code = 'if x > 5 while y < 10 + z "Hello, World" !true [ ] { } miVariable++ == tuVariable[5]] su_variable = 8+9'
file = "i.txt"
#OPen file
f = open(file, "r")
source_code = f.read()

# Llamada al analizador léxico
tokens_leguaje = tokens.Tokens.tokens
mi_lexer = Lexer(tokens_leguaje, source_code)


tokens_analizados = mi_lexer.analizar()
# Imprimir los tokens encontrados
#Write tokens in file
f = open("tokens.txt", "w")
for token in tokens_analizados:
    f.write(str(token))
    f.write("\n")
for token in tokens_analizados:
    print(token)


mi_lexer.print_symbol_table()