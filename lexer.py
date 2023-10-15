import re
import tokens

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

class Lexer:
    def __init__(self, tokens, source_code):
        self.tokens_lenguaje = tokens
        self.source_code = source_code
        self.position = 0
        self.desplazamiento = 0
        self.token_list = []
    def get_desplazamiento(self):
        return self.desplazamiento
    def get_token_list(self):
        return self.token_list
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
                        attribute = self.desplazamiento
                        self.desplazamiento += 1 #Hay que cambiarlo por el desplazamiento de la tabla de simbolos
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
file = "in3.txt"
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
