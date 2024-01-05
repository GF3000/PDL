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
19: {'V': 35},
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
62: {'B': 65,'S': 4,'C': 63},
65: {'B': 65,'S': 4,'C': 78},
66: {'E': 97,'R': 18,'U': 20,'V': 21,'D': 22},
67: {'E': 43,'R': 18,'U': 20,'V': 21,'D': 22,'L': 68},
75: {'B': 65,'C': 76},
79: {'T': 83,'A': 81},
80: {'T': 87,'H': 85},
84: {'K': 88},
89: {'T': 90},
91: {'K': 92},
    }

    def get_tabla_GOTO():
        return Tabla_GOTO.tabla_GOTO
    
class Tabla_ACCION:
    DESPLAZA = Constantes.DESPLAZA
    REDUCE = Constantes.REDUCE
    EXITO = Constantes.EXITO

    tabla_ACCION = {
        0: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], 'EOF': [REDUCE, 3]},
1: {'EOF': [EXITO, None]},
2: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], 'EOF': [REDUCE, 3]},
3: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], 'EOF': [REDUCE, 3]},
4: {'if': [REDUCE, 5], 'let': [REDUCE, 5], 'for': [REDUCE, 5], 'id': [REDUCE, 5], 'put': [REDUCE, 5], 'get': [REDUCE, 5], 'return': [REDUCE, 5], '}': [REDUCE, 5], 'function': [REDUCE, 5], 'EOF': [REDUCE, 5]},
5: {'parentesisabierto': [DESPLAZA, 16]},
6: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 51], 'string': [DESPLAZA, 50]},
7: {'parentesisabierto': [DESPLAZA, 53]},
8: {'=': [DESPLAZA, 66], 'parentesisabierto': [DESPLAZA, 67]},
9: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
10: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
11: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'puntoycoma': [REDUCE, 19], 'parentesisabierto': [DESPLAZA, 24]},
12: {'{': [DESPLAZA, 75]},
13: {'parentesisabierto': [DESPLAZA, 79]},
14: {'id': [DESPLAZA, 80]},
15: {'EOF': [REDUCE, 1]},
16: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
17: {'parentesiscerrado': [DESPLAZA, 30]},
18: {'menor': [DESPLAZA, 33], 'coma': [REDUCE, 20], 'puntoycoma': [REDUCE, 20], 'parentesiscerrado': [REDUCE, 20], 'EOF': [REDUCE, 20]},
19: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'parentesisabierto': [DESPLAZA, 24]},
20: {'menor': [REDUCE, 23], 'suma': [DESPLAZA, 36], 'coma': [REDUCE, 23], 'puntoycoma': [REDUCE, 23], 'parentesiscerrado': [REDUCE, 23], 'EOF': [REDUCE, 23]},
21: {'menor': [REDUCE, 25], 'suma': [REDUCE, 25], 'coma': [REDUCE, 25], 'puntoycoma': [REDUCE, 25], 'parentesiscerrado': [REDUCE, 25], 'EOF': [REDUCE, 25]},
22: {'menor': [REDUCE, 26], 'suma': [REDUCE, 26], 'coma': [REDUCE, 26], 'puntoycoma': [REDUCE, 26], 'parentesiscerrado': [REDUCE, 26], 'EOF': [REDUCE, 26]},
23: {'menor': [REDUCE, 27], 'suma': [REDUCE, 27], 'coma': [REDUCE, 27], 'puntoycoma': [REDUCE, 27], 'parentesisabierto': [DESPLAZA, 38], 'parentesiscerrado': [REDUCE, 27], 'EOF': [REDUCE, 27]},
24: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
25: {'id': [DESPLAZA, 31]},
26: {'menor': [REDUCE, 30], 'suma': [REDUCE, 30], 'coma': [REDUCE, 30], 'puntoycoma': [REDUCE, 30], 'parentesiscerrado': [REDUCE, 30], 'EOF': [REDUCE, 30]},
27: {'menor': [REDUCE, 31], 'suma': [REDUCE, 31], 'coma': [REDUCE, 31], 'puntoycoma': [REDUCE, 31], 'parentesiscerrado': [REDUCE, 31], 'EOF': [REDUCE, 31]},
28: {'menor': [REDUCE, 32], 'suma': [REDUCE, 32], 'coma': [REDUCE, 32], 'puntoycoma': [REDUCE, 32], 'parentesiscerrado': [REDUCE, 32], 'EOF': [REDUCE, 32]},
29: {'menor': [REDUCE, 33], 'suma': [REDUCE, 33], 'coma': [REDUCE, 33], 'puntoycoma': [REDUCE, 33], 'parentesiscerrado': [REDUCE, 33], 'EOF': [REDUCE, 33]},
30: {'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11]},
31: {'menor': [REDUCE, 34], 'suma': [REDUCE, 34], 'coma': [REDUCE, 34], 'puntoycoma': [REDUCE, 34], 'parentesiscerrado': [REDUCE, 34], 'EOF': [REDUCE, 34]},
32: {'if': [REDUCE, 17], 'let': [REDUCE, 17], 'for': [REDUCE, 17], 'id': [REDUCE, 17], 'put': [REDUCE, 17], 'get': [REDUCE, 17], 'return': [REDUCE, 17], 'parentesiscerrado': [REDUCE, 17], 'function': [REDUCE, 17], 'EOF': [REDUCE, 17]},
33: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
34: {'menor': [REDUCE, 21], 'suma': [DESPLAZA, 36], 'coma': [REDUCE, 21], 'puntoycoma': [REDUCE, 21], 'parentesiscerrado': [REDUCE, 21], 'EOF': [REDUCE, 21]},
35: {'menor': [REDUCE, 22], 'suma': [REDUCE, 22], 'coma': [REDUCE, 22], 'puntoycoma': [REDUCE, 22], 'parentesiscerrado': [REDUCE, 22], 'EOF': [REDUCE, 22]},
36: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'parentesisabierto': [DESPLAZA, 24]},
37: {'menor': [REDUCE, 24], 'suma': [REDUCE, 24], 'coma': [REDUCE, 24], 'puntoycoma': [REDUCE, 24], 'parentesiscerrado': [REDUCE, 24], 'EOF': [REDUCE, 24]},
38: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
39: {'coma': [DESPLAZA, 45], 'parentesiscerrado': [REDUCE, 37]},
40: {'parentesiscerrado': [REDUCE, 36]},
41: {'parentesiscerrado': [DESPLAZA, 42]},
42: {'menor': [REDUCE, 29], 'suma': [REDUCE, 29], 'coma': [REDUCE, 29], 'puntoycoma': [REDUCE, 29], 'parentesiscerrado': [REDUCE, 29], 'EOF': [REDUCE, 29]},
43: {'coma': [DESPLAZA, 45], 'parentesiscerrado': [REDUCE, 37]},
44: {'parentesiscerrado': [REDUCE, 35]},
45: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
46: {'id': [DESPLAZA, 47]},
47: {'puntoycoma': [DESPLAZA, 48]},
48: {'if': [REDUCE, 6], 'let': [REDUCE, 6], 'for': [REDUCE, 6], 'id': [REDUCE, 6], 'put': [REDUCE, 6], 'get': [REDUCE, 6], 'return': [REDUCE, 6], '}': [REDUCE, 6], 'function': [REDUCE, 6], 'EOF': [REDUCE, 6]},
49: {'id': [REDUCE, 10], 'parentesisabierto': [REDUCE, 10], 'EOF': [REDUCE, 10]},
50: {'id': [REDUCE, 12], 'parentesisabierto': [REDUCE, 12], 'EOF': [REDUCE, 12]},
51: {'id': [REDUCE, 11], 'parentesisabierto': [REDUCE, 11], 'EOF': [REDUCE, 11]},
52: {'=': [DESPLAZA, 54]},
53: {'id': [DESPLAZA, 52]},
54: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
55: {'puntoycoma': [DESPLAZA, 57]},
56: {'puntoycoma': [REDUCE, 8]},
57: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
58: {'puntoycoma': [DESPLAZA, 59]},
59: {'--': [DESPLAZA, 25]},
60: {'parentesiscerrado': [DESPLAZA, 61]},
61: {'{': [DESPLAZA, 62]},
62: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], '}': [REDUCE, 49]},
63: {'}': [DESPLAZA, 64]},
64: {'if': [REDUCE, 7], 'let': [REDUCE, 7], 'for': [REDUCE, 7], 'id': [REDUCE, 7], 'put': [REDUCE, 7], 'get': [REDUCE, 7], 'return': [REDUCE, 7], '}': [REDUCE, 7], 'function': [REDUCE, 7], 'EOF': [REDUCE, 7]},
65: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], '}': [REDUCE, 49]},
66: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
67: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], '--': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
68: {'parentesiscerrado': [DESPLAZA, 69]},
69: {'puntoycoma': [DESPLAZA, 70]},
70: {'if': [REDUCE, 14], 'let': [REDUCE, 14], 'for': [REDUCE, 14], 'id': [REDUCE, 14], 'put': [REDUCE, 14], 'get': [REDUCE, 14], 'return': [REDUCE, 14], '}': [REDUCE, 14], 'function': [REDUCE, 14], 'EOF': [REDUCE, 14]},
71: {'puntoycoma': [DESPLAZA, 98]},
72: {'puntoycoma': [DESPLAZA, 100]},
73: {'puntoycoma': [DESPLAZA, 32]},
74: {'puntoycoma': [REDUCE, 18]},
75: {'if': [DESPLAZA, 5], 'let': [DESPLAZA, 6], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], '}': [REDUCE, 49]},
76: {'}': [DESPLAZA, 77]},
77: {'if': [REDUCE, 38], 'let': [REDUCE, 38], 'for': [REDUCE, 38], 'id': [REDUCE, 38], 'put': [REDUCE, 38], 'get': [REDUCE, 38], 'return': [REDUCE, 38], 'function': [REDUCE, 38], 'EOF': [REDUCE, 38]},
78: {'}': [REDUCE, 48]},
79: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51], 'parentesiscerrado': [REDUCE, 45]},
80: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51], 'void': [DESPLAZA, 86]},
81: {'parentesiscerrado': [DESPLAZA, 82]},
82: {'{': [REDUCE, 39]},
83: {'id': [DESPLAZA, 84]},
84: {'coma': [DESPLAZA, 89], 'parentesiscerrado': [REDUCE, 47]},
85: {'parentesisabierto': [REDUCE, 40]},
86: {'parentesisabierto': [REDUCE, 42]},
87: {'parentesisabierto': [REDUCE, 41]},
88: {'parentesiscerrado': [REDUCE, 44]},
89: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51]},
90: {'id': [DESPLAZA, 91]},
91: {'coma': [DESPLAZA, 89], 'parentesiscerrado': [REDUCE, 47]},
92: {'parentesiscerrado': [REDUCE, 46]},
93: {'if': [REDUCE, 2], 'let': [REDUCE, 2], 'for': [REDUCE, 2], 'id': [REDUCE, 2], 'put': [REDUCE, 2], 'get': [REDUCE, 2], 'return': [REDUCE, 2], 'function': [REDUCE, 2], 'EOF': [REDUCE, 2]},
94: {'if': [REDUCE, 4], 'let': [REDUCE, 4], 'for': [REDUCE, 4], 'id': [REDUCE, 4], 'put': [REDUCE, 4], 'get': [REDUCE, 4], 'return': [REDUCE, 4], '}': [REDUCE, 4], 'function': [REDUCE, 4], 'EOF': [REDUCE, 4]},
95: {'parentesiscerrado': [DESPLAZA, 96]},
96: {'menor': [REDUCE, 28], 'suma': [REDUCE, 28], 'coma': [REDUCE, 28], 'puntoycoma': [REDUCE, 28], 'parentesiscerrado': [REDUCE, 28], 'EOF': [REDUCE, 28]},
97: {'puntoycoma': [DESPLAZA, 99]},
98: {'if': [REDUCE, 15], 'let': [REDUCE, 15], 'for': [REDUCE, 15], 'id': [REDUCE, 15], 'put': [REDUCE, 15], 'get': [REDUCE, 15], 'return': [REDUCE, 15], '}': [REDUCE, 15], 'function': [REDUCE, 15], 'EOF': [REDUCE, 15]},
99: {'if': [REDUCE, 13], 'let': [REDUCE, 13], 'for': [REDUCE, 13], 'id': [REDUCE, 13], 'put': [REDUCE, 13], 'get': [REDUCE, 13], 'return': [REDUCE, 13], '}': [REDUCE, 13], 'function': [REDUCE, 13], 'EOF': [REDUCE, 13]},
100: {'if': [REDUCE, 16], 'let': [REDUCE, 16], 'for': [REDUCE, 16], 'id': [REDUCE, 16], 'put': [REDUCE, 16], 'get': [REDUCE, 16], 'return': [REDUCE, 16], '}': [REDUCE, 16], 'function': [REDUCE, 16], 'EOF': [REDUCE, 16]}
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
<<<<<<< HEAD
    4: REGLA( 'B', ['if', 'parentesisabierto', 'E', 'parentesiscerrado', 'S']),
    5: REGLA( 'B', ['S']),
    6: REGLA( 'B', ['let', 'T', 'id', 'puntoycoma']),
    7: REGLA( 'B', ['for', 'parentesisabierto', 'Y', 'puntoycoma', 'E', 'puntoycoma', 'D', 'parentesiscerrado', '{', 'C', '}']),
=======
    4: REGLA( 'B', ['if', '(', 'E', ')', 'S']),
    5: REGLA( 'B', ['S']),
    6: REGLA( 'B', ['let', 'T', 'id', ';']),
    7: REGLA( 'B', ['for', '(', 'Y', ';', 'E', ';', 'D', ')', '{', 'C', '}']),
>>>>>>> 76ec601047be36a08c6060d6f11b4b4ce7b7d26d
    8: REGLA( 'Y', ['id', '=', 'E']),
    10: REGLA( 'T', ['int']),
    11: REGLA( 'T', ['boolean']),
    12: REGLA( 'T', ['string']),
<<<<<<< HEAD
    13: REGLA( 'S', ['id', '=', 'E', 'puntoycoma']),
    14: REGLA( 'S', ['id', 'parentesisabierto', 'L', 'parentesiscerrado', 'puntoycoma']),
    15: REGLA( 'S', ['put', 'E', 'puntoycoma']),
    16: REGLA( 'S', ['get', 'E', 'puntoycoma']),
    17: REGLA( 'S', ['return', 'X', 'puntoycoma']),
    18: REGLA( 'X', ['E']),
    19: REGLA( 'X', []),
    20: REGLA( 'E', ['R']),
    21: REGLA( 'R', ['R', 'menor', 'U']),
    22: REGLA( 'U', ['negacion', 'V']),
    23: REGLA( 'R', ['U']),
    24: REGLA( 'U', ['U', 'suma', 'V']),
    25: REGLA( 'U', ['V']),
    26: REGLA( 'U', ['D']),
    27: REGLA( 'V', ['id']),
    28: REGLA( 'V', ['parentesisabierto', 'E', 'parentesiscerrado']),
    29: REGLA( 'V', ['id', 'parentesisabierto', 'L', 'parentesiscerrado']),
=======
    13: REGLA( 'S', ['id', '=', 'E', ';']),
    14: REGLA( 'S', ['id', '(', 'L', ')', ';']),
    15: REGLA( 'S', ['put', 'E', ';']),
    16: REGLA( 'S', ['get', 'E', ';']),
    17: REGLA( 'S', ['return', 'X', ';']),
    18: REGLA( 'X', ['E']),
    19: REGLA( 'X', []),
    20: REGLA( 'E', ['R']),
    21: REGLA( 'R', ['R', '<', 'U']),
    22: REGLA( 'U', ['!', 'V']),
    23: REGLA( 'R', ['U']),
    24: REGLA( 'U', ['U', '+', 'V']),
    25: REGLA( 'U', ['V']),
    26: REGLA( 'U', ['D']),
    27: REGLA( 'V', ['id']),
    28: REGLA( 'V', ['(', 'E', ')']),
    29: REGLA( 'V', ['id', '(', 'L', ')']),
>>>>>>> 76ec601047be36a08c6060d6f11b4b4ce7b7d26d
    30: REGLA( 'V', ['entero']),
    31: REGLA( 'V', ['cadena']),
    32: REGLA( 'V', ['true']),
    33: REGLA( 'V', ['false']),
    34: REGLA( 'D', ['--', 'id']),
    35: REGLA( 'L', ['E', 'Q']),
<<<<<<< HEAD
    36: REGLA( 'Q', ['coma', 'E', 'Q']),
    37: REGLA( 'Q', []),
    38: REGLA( 'F', ['F1', '{', 'C', '}']),
    39: REGLA( 'F1', ['F2', 'parentesisabierto', 'A', 'parentesiscerrado']),
=======
    36: REGLA( 'Q', [',', 'E', 'Q']),
    37: REGLA( 'Q', []),
    38: REGLA( 'F', ['F1', '{', 'C', '}']),
    39: REGLA( 'F1', ['F2', '(', 'A', ')']),
>>>>>>> 76ec601047be36a08c6060d6f11b4b4ce7b7d26d
    40: REGLA( 'F2', ['function', 'id', 'H']),
    41: REGLA( 'H', ['T']),
    42: REGLA( 'H', ['void']),
    43: REGLA( 'H', []),
    44: REGLA( 'A', ['T', 'id', 'K']),
    45: REGLA( 'A', []),
<<<<<<< HEAD
    46: REGLA( 'K', ['coma', 'T', 'id', 'K']),
=======
    46: REGLA( 'K', [',', 'T', 'id', 'K']),
>>>>>>> 76ec601047be36a08c6060d6f11b4b4ce7b7d26d
    47: REGLA( 'K', []),
    48: REGLA( 'C', ['B', 'C']),
    49: REGLA( 'C', [])
    }
    
    def get_reglas():
        return Reglas.reglas