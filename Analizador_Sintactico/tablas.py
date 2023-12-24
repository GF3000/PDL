#Constantes
class Constantes:
    REDUCE = 0
    DESPLAZA = 1
    EXITO = 2
    DESCRIPTORES = {REDUCE: "REDUCE", DESPLAZA: "DESPLAZA", EXITO: "EXITO"} # Para imprimir el tipo de accion


class Tabla_GOTO:
    tabla_GOTO = {
    0: {'P': 1,'B': 2,'S': 4,'F': 3,'F1': 12,'F2': 13},
    2: {'P': 15,'B': 2,'S': 4,'F': 3,'F1': 12,'F2': 13},
    3: {'P': 93,'B': 2,'S': 4,'F': 3,'F1': 12,'F2': 13},
    6: {'T': 46},
    9: {'E': 71,'R': 18,'U': 20,'V': 21,'D': 22},
    10: {'E': 72,'R': 18,'U': 20,'V': 21,'D': 22},
    11: {'X': 73,'E': 74,'R': 18,'U': 20,'V': 21,'D': 22},
    16: {'E': 17,'R': 18,'U': 20,'V': 21,'D': 22},
    19: {'U': 35,'V': 21,'D': 22},
    24: {'E': 95,'R': 18,'U': 20,'V': 21,'D': 22},
    30: {'S': 94},
    33: {'U': 34,'V': 21,'D': 22},
    36: {'V': 37},
    38: {'E': 43,'R': 18,'U': 20,'V': 21,'D': 22,'L': 41},
    39: {'Q': 40},
    43: {'Q': 44},
    45: {'E': 39,'R': 18,'U': 20,'V': 21,'D': 22},
    53: {'Y': 55},
    54: {'E': 56,'R': 18,'U': 20,'V': 21,'D': 22},
    57: {'E': 58,'R': 18,'U': 20,'V': 21,'D': 22},
    59: {'D': 60},
    62: {'B': 65,'C': 63},
    65: {'B': 65,'C': 78},
    66: {'E': 97,'R': 18,'U': 20,'V': 21,'D': 22},
    67: {'E': 43,'R': 18,'U': 20,'V': 21,'D': 22,'L': 68},
    75: {'B': 65,'C': 76},
    79: {'T': 83,'A': 81},
    80: {'T': 87,'H': 85},
    84: {'K': 88},
    89: {'T': 90},
    91: {'K': 92}
    }

    def get_tabla_GOTO():
        return Tabla_GOTO.tabla_GOTO
    
class Tabla_ACCION:
    DESPLAZA = Constantes.DESPLAZA
    REDUCE = Constantes.REDUCE
    EXITO = Constantes.EXITO

    tabla_ACCION = {
    0: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], '$': [REDUCE, 3]},
    1: {'$': [EXITO, None]},
    2: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], '$': [REDUCE, 3]},
    3: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], '$': [REDUCE, 3]},
    4: {'if': [REDUCE, 5], 'let': [REDUCE, 5], 'for': [REDUCE, 5], 'id': [REDUCE, 5], 'put': [REDUCE, 5], 'get': [REDUCE, 5], 'return': [REDUCE, 5], 'function': [REDUCE, 5], '$': [REDUCE, 5]},
    5: {'(': [DESPLAZA, 16]},
    6: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 51], 'string': [DESPLAZA, 50]},
    7: {'(': [DESPLAZA, 52]},
    8: {'=': [DESPLAZA, 66], '(': [DESPLAZA, 67]},
    9: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    10: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    11: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], ';': [REDUCE, 19], '(': [DESPLAZA, 24], '$': [REDUCE, 19]},
    12: {'{': [DESPLAZA, 75]},
    13: {'(': [DESPLAZA, 79]},
    14: {'id': [DESPLAZA, 80]},
    15: {'$': [REDUCE, 1]},
    16: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    17: {')': [DESPLAZA, 30]},
    18: {'<': [DESPLAZA, 33], ',': [REDUCE, 20], ';': [REDUCE, 20], ')': [REDUCE, 20], '$': [REDUCE, 20]},
    19: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    20: {'<': [REDUCE, 23], '+': [DESPLAZA, 36], ',': [REDUCE, 23], ';': [REDUCE, 23], ')': [REDUCE, 23], '$': [REDUCE, 23]},
    21: {'<': [REDUCE, 25], '+': [REDUCE, 25], ',': [REDUCE, 25], ';': [REDUCE, 25], ')': [REDUCE, 25], '$': [REDUCE, 25]},
    22: {'<': [REDUCE, 26], '+': [REDUCE, 26], ',': [REDUCE, 26], ';': [REDUCE, 26], ')': [REDUCE, 26], '$': [REDUCE, 26]},
    23: {'<': [REDUCE, 27], '+': [REDUCE, 27], ',': [REDUCE, 27], ';': [REDUCE, 27], '(': [DESPLAZA, 38], ')': [REDUCE, 27], '$': [REDUCE, 27]},
    24: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    25: {'id': [DESPLAZA, 31]},
    26: {'<': [REDUCE, 30], '+': [REDUCE, 30], ',': [REDUCE, 30], ';': [REDUCE, 30], ')': [REDUCE, 30], '$': [REDUCE, 30]},
    27: {'<': [REDUCE, 31], '+': [REDUCE, 31], ',': [REDUCE, 31], ';': [REDUCE, 31], ')': [REDUCE, 31], '$': [REDUCE, 31]},
    28: {'<': [REDUCE, 32], '+': [REDUCE, 32], ',': [REDUCE, 32], ';': [REDUCE, 32], ')': [REDUCE, 32], '$': [REDUCE, 32]},
    29: {'<': [REDUCE, 33], '+': [REDUCE, 33], ',': [REDUCE, 33], ';': [REDUCE, 33], ')': [REDUCE, 33], '$': [REDUCE, 33]},
    30: {'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11]},
    31: {'<': [REDUCE, 34], '+': [REDUCE, 34], ',': [REDUCE, 34], ';': [REDUCE, 34], ')': [REDUCE, 34], '$': [REDUCE, 34]},
    32: {'if': [REDUCE, 17], 'let': [REDUCE, 17], 'for': [REDUCE, 17], 'id': [REDUCE, 17], 'put': [REDUCE, 17], 'get': [REDUCE, 17], 'return': [REDUCE, 17], 'function': [REDUCE, 17], '$': [REDUCE, 17]},
    33: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    34: {'<': [REDUCE, 21], '+': [DESPLAZA, 36], ',': [REDUCE, 21], ';': [REDUCE, 21], ')': [REDUCE, 21], '$': [REDUCE, 21]},
    35: {'<': [REDUCE, 22], '+': [DESPLAZA, 36], ',': [REDUCE, 22], ';': [REDUCE, 22], ')': [REDUCE, 22], '$': [REDUCE, 22]},
    36: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '(': [DESPLAZA, 24]},
    37: {'<': [REDUCE, 24], '+': [REDUCE, 24], ',': [REDUCE, 24], ';': [REDUCE, 24], ')': [REDUCE, 24], '$': [REDUCE, 24]},
    38: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    39: {',': [DESPLAZA, 45], ')': [REDUCE, 37]},
    40: {')': [REDUCE, 36]},
    41: {')': [DESPLAZA, 42]},
    42: {'<': [REDUCE, 29], '+': [REDUCE, 29], ',': [REDUCE, 29], ';': [REDUCE, 29], ')': [REDUCE, 29], '$': [REDUCE, 29]},
    43: {',': [DESPLAZA, 45], ')': [REDUCE, 37]},
    44: {')': [REDUCE, 35]},
    45: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    46: {'id': [DESPLAZA, 47]},
    47: {';': [DESPLAZA, 48]},
    48: {'if': [REDUCE, 6], 'let': [REDUCE, 6], 'for': [REDUCE, 6], 'id': [REDUCE, 6], 'put': [REDUCE, 6], 'get': [REDUCE, 6], 'return': [REDUCE, 6], 'function': [REDUCE, 6], '$': [REDUCE, 6]},
    49: {'id': [REDUCE, 10], '(': [REDUCE, 10], '$': [REDUCE, 10]},
    50: {'id': [REDUCE, 12], '(': [REDUCE, 12], '$': [REDUCE, 12]},
    51: {'id': [REDUCE, 11], '(': [REDUCE, 11], '$': [REDUCE, 11]},
    52: {'id': [DESPLAZA, 53]},
    53: {'=': [DESPLAZA, 54], ';': [REDUCE, 9]},
    54: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    55: {';': [DESPLAZA, 57]},
    56: {';': [REDUCE, 8]},
    57: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    58: {';': [DESPLAZA, 59]},
    59: {'--': [DESPLAZA, 25]},
    60: {')': [DESPLAZA, 61]},
    61: {'{': [DESPLAZA, 62]},
    62: {'for': [DESPLAZA, 7], '}': [REDUCE, 49]},
    63: {'}': [DESPLAZA, 64]},
    64: {'if': [REDUCE, 7], 'let': [REDUCE, 7], 'for': [REDUCE, 7], 'id': [REDUCE, 7], 'put': [REDUCE, 7], 'get': [REDUCE, 7], 'return': [REDUCE, 7], 'function': [REDUCE, 7], '$': [REDUCE, 7]},
    65: {'}': [REDUCE, 49]},
    66: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    67: {'id': [DESPLAZA, 23], '!': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], '(': [DESPLAZA, 24]},
    68: {')': [DESPLAZA, 69]},
    69: {';': [DESPLAZA, 70]},
    70: {'if': [REDUCE, 14], 'let': [REDUCE, 14], 'for': [REDUCE, 14], 'id': [REDUCE, 14], 'put': [REDUCE, 14], 'get': [REDUCE, 14], 'return': [REDUCE, 14], 'function': [REDUCE, 14], '$': [REDUCE, 14]},
    71: {';': [DESPLAZA, 98]},
    72: {';': [DESPLAZA, 100]},
    73: {';': [DESPLAZA, 32]},
    74: {';': [REDUCE, 18]},
    75: {'}': [REDUCE, 49]},
    76: {'}': [DESPLAZA, 77]},
    77: {'if': [REDUCE, 38], 'let': [REDUCE, 38], 'for': [REDUCE, 38], 'id': [REDUCE, 38], 'put': [REDUCE, 38], 'get': [REDUCE, 38], 'return': [REDUCE, 38], 'function': [REDUCE, 38], '$': [REDUCE, 38]},
    78: {'}': [REDUCE, 48]},
    79: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51], ')': [REDUCE, 45]},
    80: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51], 'void': [DESPLAZA, 86]},
    81: {')': [DESPLAZA, 82]},
    82: {'{': [REDUCE, 39]},
    83: {'id': [DESPLAZA, 84]},
    84: {',': [DESPLAZA, 89], ')': [REDUCE, 47]},
    85: {'(': [REDUCE, 40]},
    86: {'(': [REDUCE, 42]},
    87: {'(': [REDUCE, 41]},
    88: {')': [REDUCE, 44]},
    89: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51]},
    90: {'id': [DESPLAZA, 91]},
    91: {',': [DESPLAZA, 89], ')': [REDUCE, 47]},
    92: {')': [REDUCE, 46]},
    93: {'$': [REDUCE, 2]},
    94: {'if': [REDUCE, 4], 'let': [REDUCE, 4], 'for': [REDUCE, 4], 'id': [REDUCE, 4], 'put': [REDUCE, 4], 'get': [REDUCE, 4], 'return': [REDUCE, 4], 'function': [REDUCE, 4], '$': [REDUCE, 4]},
    95: {')': [DESPLAZA, 96]},
    96: {'<': [REDUCE, 28], '+': [REDUCE, 28], ',': [REDUCE, 28], ';': [REDUCE, 28], ')': [REDUCE, 28], '$': [REDUCE, 28]},
    97: {';': [DESPLAZA, 99]},
    98: {'if': [REDUCE, 15], 'let': [REDUCE, 15], 'for': [REDUCE, 15], 'id': [REDUCE, 15], 'put': [REDUCE, 15], 'get': [REDUCE, 15], 'return': [REDUCE, 15], 'function': [REDUCE, 15], '$': [REDUCE, 15]},
    99: {'if': [REDUCE, 13], 'let': [REDUCE, 13], 'for': [REDUCE, 13], 'id': [REDUCE, 13], 'put': [REDUCE, 13], 'get': [REDUCE, 13], 'return': [REDUCE, 13], 'function': [REDUCE, 13], '$': [REDUCE, 13]},
    100: {'if': [REDUCE, 16], 'let': [REDUCE, 16], 'for': [REDUCE, 16], 'id': [REDUCE, 16], 'put': [REDUCE, 16], 'get': [REDUCE, 16], 'return': [REDUCE, 16], 'function': [REDUCE, 16], '$': [REDUCE, 16]},
    }
    def get_tabla_ACCION():
        return Tabla_ACCION.tabla_ACCION

#Clase correspondiente al analizador sintactico para un analizador sintactico ascendente
class REGLA:
    """Clase correspondiente a una regla de produccion"""

    def __init__(self, izquierda, derecha):
        """Inicializa la regla de produccion. izquierda es el simbolo no terminal de la izquierda y derecha es una lista de simbolos terminales y no terminales producidos"""
        self.izquierda = izquierda
        self.derecha = derecha
    def __str__(self):
        parte_derecha = ""
        for simbolo in self.derecha:
            parte_derecha += simbolo + " "
        return self.izquierda + " -> " + parte_derecha
    
class Reglas:
    reglas = {
    1: REGLA( 'P', ['B', 'P']),
    2: REGLA( 'P', ['F', 'P']),
    3: REGLA( 'P', []),
    4: REGLA( 'B', ['if', '(', 'E', ')', 'S']),
    5: REGLA( 'B', ['S']),
    6: REGLA( 'B', ['let', 'T', 'id', ';']),
    7: REGLA( 'B', ['for', '(', 'id', 'Y', ';', 'E', ';', 'D', ')', '{', 'C', '}']),
    8: REGLA( 'Y', ['=', 'E']),
    9: REGLA( 'Y', []),
    10: REGLA( 'T', ['int']),
    11: REGLA( 'T', ['boolean']),
    12: REGLA( 'T', ['string']),
    13: REGLA( 'S', ['id', '=', 'E', ';']),
    14: REGLA( 'S', ['id', '(', 'L', ')', ';']),
    15: REGLA( 'S', ['put', 'E', ';']),
    16: REGLA( 'S', ['get', 'E', ';']),
    17: REGLA( 'S', ['return', 'X', ';']),
    18: REGLA( 'X', ['E']),
    19: REGLA( 'X', []),
    20: REGLA( 'E', ['R']),
    21: REGLA( 'R', ['R', '<', 'U']),
    22: REGLA( 'R', ['!', 'U']),
    23: REGLA( 'R', ['U']),
    24: REGLA( 'U', ['U', '+', 'V']),
    25: REGLA( 'U', ['V']),
    26: REGLA( 'U', ['D']),
    27: REGLA( 'V', ['id']),
    28: REGLA( 'V', ['(', 'E', ')']),
    29: REGLA( 'V', ['id', '(', 'L', ')']),
    30: REGLA( 'V', ['entero']),
    31: REGLA( 'V', ['cadena']),
    32: REGLA( 'V', ['true']),
    33: REGLA( 'V', ['false']),
    34: REGLA( 'D', ['--', 'id']),
    35: REGLA( 'L', ['E', 'Q']),
    36: REGLA( 'Q', [',', 'E', 'Q']),
    37: REGLA( 'Q', []),
    38: REGLA( 'F', ['F1', '{', 'C', '}']),
    39: REGLA( 'F1', ['F2', '(', 'A', ')']),
    40: REGLA( 'F2', ['function', 'id', 'H']),
    41: REGLA( 'H', ['T']),
    42: REGLA( 'H', ['void']),
    43: REGLA( 'H', []),
    44: REGLA( 'A', ['T', 'id', 'K']),
    45: REGLA( 'A', []),
    46: REGLA( 'K', [',', 'T', 'id', 'K']),
    47: REGLA( 'K', []),
    48: REGLA( 'C', ['B', 'C']),
    49: REGLA( 'C', [])
    }
    
    def get_reglas():
        return Reglas.reglas