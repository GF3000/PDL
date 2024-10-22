# Todos los tokens del lenguaje

class Tokens:
    """Defincion de los Tokens usados en nuestra Prcatica"""
    tokens = [
    # Token, atributo, expresión regular
            
    # Sin atributos
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
    ('parentesisabierto', None, r'\('),
    ('parentesiscerrado', None, r'\)'),
    ('llaveabierta', None, r'\{'),
    ('llavecerrada', None, r'\}'),
    ('suma', None, r'\+'),
    ('negacion', None, r'\!'),
    ('menor', None, r'\<'),
    ('false', None, r'\bfalse\b'),
    ('true', None, r'\btrue\b'),
    ('EOF', None, r'\$'), #Token de fin de fichero

    
    # Con atributos
    ('entero', None, r'[+-]?\d+'), #Lee entero con y sin signo
    ('id', None, r'[a-zA-Z_]\w*'), #Lee identificadores
    ('cadena', None, r'\'[^\']*\''), #Lee cadenas con comillas simples o dobles

    # Conentarios
    ('comentario', None, r'//.*\n'),

    ]
    def get_tokens():
        return Tokens.tokens