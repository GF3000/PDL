class Tokens:
    """Defincion de los Tokens usados en nuestra Prcatica"""
    tokens = [
    # Token, atributo, expresión regular

# boolean 
# for 
# function 
# get
# if
# int 
# let 
# put
# return 
# string 
# void 




    # Palabras reservadas
    #Se añade el \b para asegurarse que las palabras están rodeadas de espacios
    ('boolean', None, r'\bboolean\b'),
    ('for', None, r'\bfor\b'),
    ('function', None, r'\bfunction\b'),
    ('get', None, r'\bget\b'),
    ('if', None, r'\bif\b'),
    ('int', None, r'\bint\b'),
    ('let', None, r'\blet\b'),
    ('put', None, r'\bput\b'),
    ('return', None, r'\breturn\b'),
    ('string', None, r'\bstring\b'),
    ('void', None, r'\bvoid\b'),
    ('autodecremento', None, r'\-\-'),
    ('asignacion', None, r'\='),
    ('coma', None, r'\,'),
    ('puntoycoma', None, r'\;'),
    ('paretesisabierto', None, r'\('),
    ('parentesiscerrado', None, r'\)'),
    ('llaaveabierta', None, r'\{'),
    ('llavecerrada', None, r'\}'),
    ('suma', None, r'\+'),
    ('negacion', None, r'\!'),
    ('menor', None, r'\<'),
    ('false', None, r'\false\b'),
    ('true', None, r'\true\b'),
    ('entero', None, r'\d+'),
    ('EOF', None, r'\$'), #Token de fin de fichero

    
    # Con atributos
    ('entero', None, r'[+-]?\d+'), #Lee entero con y sin signo
    ('id', None, r'[a-zA-Z_]\w*'), #Lee identificadores
    ('cadena', None, r'(\'[^\']*\'|\"[^\"]*\")') #Lee cadenas con comillas simples o dobles
    ]
    def get_tokens():
        return Tokens.tokens