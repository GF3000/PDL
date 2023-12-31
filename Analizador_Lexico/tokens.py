class Tokens:
    """Defincion de los Tokens usados en nuestra Prcatica"""
    tokens = [
    # Token, atributo, expresión regular

    # Palabras reservadas
    #Se añade el \b para asegurarse que las palabras están rodeadas de espacios
    ('if', None, r'\bif\b'),
    ('PalRes', 'while', r'\bwhile\b'),
    ('for', None, r'\bfor\b'),
    ("PalRes", "get", r'\bget\b'),
    ("PalRes", "put", r'\bput\b'),
    ("PalRes", "return", r'\breturn\b'),
    ("let", None, r'\blet\b'),
    ("PalRes", "int", r'\bint\b'),
    ("PalRes", "float", r'\bfloat\b'),
    ("PalRes", "string", r'\bstring\b'),
    ("PalRes", "boolean", r'\bboolean\b'),
    ("PalRes", "function", r'\bfunction\b'),
    ("PalRes", "void", r'\bvoid\b'),


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
    
    # Con atributos
    ('INTEGER', None, r'\d+'),
    ('IDENTIFIER', None, r'[a-zA-Z_]\w*'),
    ('CAD', None, r"'[^']*'"),
    ('CAD', None, r'"[^"]*"') 
    ]
    def get_tokens():
        return Tokens.tokens