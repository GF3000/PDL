class Tokens:
    """Defincion de los Tokens usados en nuestra Prcatica"""
    tokens = [
    # Token, atributo, expresión regular

    # Palabras reservadas
    ('PalRes', 'if', r'if'),
    ('PalRes', 'while', r'while'),
    ('PalRes', 'for', r'for'),
    ("PalRes", "get", r'get'),
    ("PalRes", "put", r'put'),
    ("PalRes", "return", r'return'),
    ("PalRes", "let", r'let'),
    ("PalRes", "int", r'int'),
    ("PalRes", "float", r'float'),
    ("PalRes", "string", r'string'),
    ("PalRes", "boolean", r'boolean'),
    ("PalRes", "function", r'function'),


    # Operadores
    ('OP', 'igual', r'=='),
    ('OP', 'asignacion', r'='),
    ('OP', 'incremento', r'\+\+'),
    ('OP', 'decremento', r'--'),

    ('OP', 'suma', r'\+'),
    ("OP", "multiplicacion", r'\*'),
    ('OP', 'resta', r'-'),
    ('OP', 'division', r'/'),
    ("OP", "modulo", r'%'),
    ('OP', 'and', r'&&'),
    ('OP', 'or', r'\|\|'),
    ('OP', 'not', r'!'),
    ('OP', 'diferente', r'!='),
    ('OP', 'menor', r'<'),
    ('OP', 'menorIgual', r'<='),
    ('OP', 'mayor', r'>'),
    ('OP', 'mayorIgual', r'>='),

    # Puntuación
    ("Coma", None, r','),
    ("PuntoComa", None, r';'),

    # Agrupadores
    ("IParentesis", None, r'\('),
    ("DParentesis", None, r'\)'),
    ("ILlave", None, r'\{'),
    ("DLlave", None, r'\}'),
    ("ICorchete", None, r'\['),
    ("DCorchete", None, r'\]'),

    # Otros
    ("True", None, r'true'),
    ("False", None, r'false'),
    ("EOF", None, r'EOF'),
    
    ('INTEGER', None, r'\d+'),
    ('IDENTIFIER', None, r'[a-zA-Z_]\w*'),
    ('CAD', None, r"'[^']*'")  
    ]
    def get_tokens(self):
        return self.tokens