import tabladesimbolos


#Constantes
class Constantes:
    REDUCE = 0
    DESPLAZA = 1
    EXITO = 2
    DESCRIPTORES = {REDUCE: "REDUCE", DESPLAZA: "DESPLAZA", EXITO: "EXITO"} # Para imprimir el tipo de accion


class Tabla_GOTO:
    tabla_GOTO = {
    0: {'P': 1,'B': 2,'S': 4,'F': 3,'F1': 12,'F2': 13, 'D1': 105},
2: {'P': 15,'B': 2,'S': 4,'F': 3,'F1': 12,'F2': 13, 'D1': 105},
3: {'P': 93,'B': 2,'S': 4,'F': 3,'F1': 12,'F2': 13, 'D1': 105},
6: {'T': 46},
9: {'E': 71,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
10: {'E': 72,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
11: {'X': 73,'E': 74,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
16: {'E': 17,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
19: {'V': 35},
24: {'E': 95,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
30: {'S': 94, 'D1': 105},
33: {'U': 34,'V': 21,'D': 22,'Y': 101},
36: {'V': 37},
38: {'E': 43,'R': 18,'U': 20,'V': 21,'D': 22,'L': 41,'Y': 101},
39: {'Q': 40},
43: {'Q': 44},
45: {'E': 39,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
53: {'Y': 55},
54: {'E': 56,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
57: {'E': 58,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
59: {'D': 60,'Y': 101},
62: {'B': 65,'S': 4,'C': 63, 'D1': 105},
65: {'B': 65,'S': 4,'C': 78, 'D1': 105},
66: {'E': 97,'R': 18,'U': 20,'V': 21,'D': 22,'Y': 101},
67: {'E': 43,'R': 18,'U': 20,'V': 21,'D': 22,'L': 68,'Y': 101},
75: {'B': 65,'C': 76, 'D1': 105, 'S': 4},
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
        0: {'autodecremento': [DESPLAZA, 102],'if': [DESPLAZA, 5], 'let': [DESPLAZA, 47], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], 'EOF': [REDUCE, 3]},
1: {'EOF': [EXITO, None]},
2: {'autodecremento': [DESPLAZA, 102],'if': [DESPLAZA, 5], 'let': [DESPLAZA, 47], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], 'EOF': [REDUCE, 3]},
3: {'autodecremento': [DESPLAZA, 102],'if': [DESPLAZA, 5], 'let': [DESPLAZA, 47], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'function': [DESPLAZA, 14], 'EOF': [REDUCE, 3]},
4: {'if': [REDUCE, 5], 'let': [REDUCE, 5], 'for': [REDUCE, 5], 'id': [REDUCE, 5], 'put': [REDUCE, 5], 'get': [REDUCE, 5], 'return': [REDUCE, 5], 'llavecerrada': [REDUCE, 5], 'function': [REDUCE, 5], 'EOF': [REDUCE, 5]},
5: {'parentesisabierto': [DESPLAZA, 16]},
6: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 51], 'string': [DESPLAZA, 50]},
7: {'parentesisabierto': [DESPLAZA, 53]},
8: {'asignacion': [DESPLAZA, 66], 'parentesisabierto': [DESPLAZA, 67]},
9: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
10: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
11: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'puntoycoma': [REDUCE, 19], 'parentesisabierto': [DESPLAZA, 24]},
12: {'llaveabierta': [DESPLAZA, 75]},
13: {'parentesisabierto': [DESPLAZA, 79]},
14: {'id': [DESPLAZA, 80]},
15: {'EOF': [REDUCE, 1]},
16: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
17: {'parentesiscerrado': [DESPLAZA, 30]},
18: {'menor': [DESPLAZA, 33], 'coma': [REDUCE, 20], 'puntoycoma': [REDUCE, 20], 'parentesiscerrado': [REDUCE, 20], 'EOF': [REDUCE, 20]},
19: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'parentesisabierto': [DESPLAZA, 24]},
20: {'menor': [REDUCE, 23], 'suma': [DESPLAZA, 36], 'coma': [REDUCE, 23], 'puntoycoma': [REDUCE, 23], 'parentesiscerrado': [REDUCE, 23], 'EOF': [REDUCE, 23]},
21: {'menor': [REDUCE, 25], 'suma': [REDUCE, 25], 'coma': [REDUCE, 25], 'puntoycoma': [REDUCE, 25], 'parentesiscerrado': [REDUCE, 25], 'EOF': [REDUCE, 25]},
22: {'menor': [REDUCE, 26], 'suma': [REDUCE, 26], 'coma': [REDUCE, 26], 'puntoycoma': [REDUCE, 26], 'parentesiscerrado': [REDUCE, 26], 'EOF': [REDUCE, 26]},
23: {'asignacion': [DESPLAZA, 54],'menor': [REDUCE, 27], 'suma': [REDUCE, 27], 'coma': [REDUCE, 27], 'puntoycoma': [REDUCE, 27], 'parentesisabierto': [DESPLAZA, 38], 'parentesiscerrado': [REDUCE, 27], 'EOF': [REDUCE, 27]},
24: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
25: {'id': [DESPLAZA, 31]},
26: {'menor': [REDUCE, 30], 'suma': [REDUCE, 30], 'coma': [REDUCE, 30], 'puntoycoma': [REDUCE, 30], 'parentesiscerrado': [REDUCE, 30], 'EOF': [REDUCE, 30]},
27: {'menor': [REDUCE, 31], 'suma': [REDUCE, 31], 'coma': [REDUCE, 31], 'puntoycoma': [REDUCE, 31], 'parentesiscerrado': [REDUCE, 31], 'EOF': [REDUCE, 31]},
28: {'menor': [REDUCE, 32], 'suma': [REDUCE, 32], 'coma': [REDUCE, 32], 'puntoycoma': [REDUCE, 32], 'parentesiscerrado': [REDUCE, 32], 'EOF': [REDUCE, 32]},
29: {'menor': [REDUCE, 33], 'suma': [REDUCE, 33], 'coma': [REDUCE, 33], 'puntoycoma': [REDUCE, 33], 'parentesiscerrado': [REDUCE, 33], 'EOF': [REDUCE, 33]},
30: {'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'autodecremento': [DESPLAZA, 102],'return': [DESPLAZA, 11]},
31: {'menor': [REDUCE, 34], 'suma': [REDUCE, 34], 'coma': [REDUCE, 34], 'puntoycoma': [REDUCE, 34], 'parentesiscerrado': [REDUCE, 34], 'EOF': [REDUCE, 34]},
32: {'if': [REDUCE, 17], 'let': [REDUCE, 17], 'for': [REDUCE, 17], 'id': [REDUCE, 17], 'put': [REDUCE, 17], 'get': [REDUCE, 17], 'return': [REDUCE, 17], 'parentesiscerrado': [REDUCE, 17], 'function': [REDUCE, 17], 'EOF': [REDUCE, 17]},
33: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
34: {'menor': [REDUCE, 21], 'suma': [DESPLAZA, 36], 'coma': [REDUCE, 21], 'puntoycoma': [REDUCE, 21], 'parentesiscerrado': [REDUCE, 21], 'EOF': [REDUCE, 21]},
35: {'menor': [REDUCE, 22], 'suma': [REDUCE, 22], 'coma': [REDUCE, 22], 'puntoycoma': [REDUCE, 22], 'parentesiscerrado': [REDUCE, 22], 'EOF': [REDUCE, 22]},
36: {'id': [DESPLAZA, 23], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'parentesisabierto': [DESPLAZA, 24]},
37: {'menor': [REDUCE, 24], 'suma': [REDUCE, 24], 'coma': [REDUCE, 24], 'puntoycoma': [REDUCE, 24], 'parentesiscerrado': [REDUCE, 24], 'EOF': [REDUCE, 24]},
38: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
39: {'coma': [DESPLAZA, 45], 'parentesiscerrado': [REDUCE, 37]},
40: {'parentesiscerrado': [REDUCE, 36]},
41: {'parentesiscerrado': [DESPLAZA, 42]},
42: {'menor': [REDUCE, 29], 'suma': [REDUCE, 29], 'coma': [REDUCE, 29], 'puntoycoma': [REDUCE, 29], 'parentesiscerrado': [REDUCE, 29], 'EOF': [REDUCE, 29]},
43: {'coma': [DESPLAZA, 45], 'parentesiscerrado': [REDUCE, 37]},
44: {'parentesiscerrado': [REDUCE, 35]},
45: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
46: {'puntoycoma': [DESPLAZA, 48]},
47: {'id': [DESPLAZA, 6]},
48: {'if': [REDUCE, 6], 'let': [REDUCE, 6], 'for': [REDUCE, 6], 'id': [REDUCE, 6], 'put': [REDUCE, 6], 'get': [REDUCE, 6], 'return': [REDUCE, 6], 'llavecerrada': [REDUCE, 6], 'function': [REDUCE, 6], 'EOF': [REDUCE, 6]},
49: {'id': [REDUCE , 10], 'puntoycoma': [REDUCE, 10], 'parentesisabierto': [REDUCE, 10], 'EOF': [REDUCE, 10]},
50: {'id': [REDUCE , 12], 'puntoycoma': [REDUCE, 12], 'parentesisabierto': [REDUCE, 12], 'EOF': [REDUCE, 12]},
51: {'id': [REDUCE , 11], 'puntoycoma': [REDUCE, 11], 'parentesisabierto': [REDUCE, 11], 'EOF': [REDUCE, 11]},
52: {'asignacion': [DESPLAZA, 54]},
53: {'id': [DESPLAZA, 52]},
54: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
55: {'puntoycoma': [DESPLAZA, 57]},
56: {'menor': [REDUCE, 8], 'suma': [REDUCE, 8], 'coma': [REDUCE, 8], 'puntoycoma': [REDUCE, 8], 'parentesiscerrado': [REDUCE, 8], 'EOF': [REDUCE, 8]},
57: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
58: {'puntoycoma': [DESPLAZA, 59]},
59: {'id': [DESPLAZA, 52],'autodecremento': [DESPLAZA, 25]},
60: {'parentesiscerrado': [DESPLAZA, 61]},
61: {'llaveabierta': [DESPLAZA, 62]},
62: {'autodecremento': [DESPLAZA, 102],'if': [DESPLAZA, 5], 'let': [DESPLAZA, 47], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'llavecerrada': [REDUCE, 49]},
63: {'llavecerrada': [DESPLAZA, 64]},
64: {'if': [REDUCE, 7], 'let': [REDUCE, 7], 'for': [REDUCE, 7], 'id': [REDUCE, 7], 'put': [REDUCE, 7], 'get': [REDUCE, 7], 'return': [REDUCE, 7], 'llavecerrada': [REDUCE, 7], 'function': [REDUCE, 7], 'EOF': [REDUCE, 7]},
65: {'autodecremento': [DESPLAZA, 102],'if': [DESPLAZA, 5], 'let': [DESPLAZA, 47], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'llavecerrada': [REDUCE, 49]},
66: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
67: {'id': [DESPLAZA, 23], 'negacion': [DESPLAZA, 19], 'entero': [DESPLAZA, 26], 'cadena': [DESPLAZA, 27], 'true': [DESPLAZA, 28], 'false': [DESPLAZA, 29], 'autodecremento': [DESPLAZA, 25], 'parentesisabierto': [DESPLAZA, 24]},
68: {'parentesiscerrado': [DESPLAZA, 69]},
69: {'puntoycoma': [DESPLAZA, 70]},
70: {'if': [REDUCE, 14], 'let': [REDUCE, 14], 'for': [REDUCE, 14], 'id': [REDUCE, 14], 'put': [REDUCE, 14], 'get': [REDUCE, 14], 'return': [REDUCE, 14], 'llavecerrada': [REDUCE, 14], 'function': [REDUCE, 14], 'EOF': [REDUCE, 14]},
71: {'puntoycoma': [DESPLAZA, 98]},
72: {'puntoycoma': [DESPLAZA, 100]},
73: {'puntoycoma': [DESPLAZA, 32]},
74: {'puntoycoma': [REDUCE, 18]},
75: {'if': [DESPLAZA, 5],'autodecremento': [DESPLAZA, 102], 'let': [DESPLAZA, 47], 'for': [DESPLAZA, 7], 'id': [DESPLAZA, 8], 'put': [DESPLAZA, 9], 'get': [DESPLAZA, 10], 'return': [DESPLAZA, 11], 'llavecerrada': [REDUCE, 49]},
76: {'llavecerrada': [DESPLAZA, 77]},
77: {'if': [REDUCE, 38], 'let': [REDUCE, 38], 'for': [REDUCE, 38], 'id': [REDUCE, 38], 'put': [REDUCE, 38], 'get': [REDUCE, 38], 'return': [REDUCE, 38], 'function': [REDUCE, 38], 'EOF': [REDUCE, 38]},
78: {'llavecerrada': [REDUCE, 48]},
79: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51], 'parentesiscerrado': [REDUCE, 45]},
80: {'int': [DESPLAZA, 49], 'boolean': [DESPLAZA, 50], 'string': [DESPLAZA, 51], 'void': [DESPLAZA, 86]},
81: {'parentesiscerrado': [DESPLAZA, 82]},
82: {'llaveabierta': [REDUCE, 39]},
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
94: {'if': [REDUCE, 4], 'let': [REDUCE, 4], 'for': [REDUCE, 4], 'id': [REDUCE, 4], 'put': [REDUCE, 4], 'get': [REDUCE, 4], 'return': [REDUCE, 4], 'llavecerrada': [REDUCE, 4], 'function': [REDUCE, 4], 'EOF': [REDUCE, 4]},
95: {'parentesiscerrado': [DESPLAZA, 96]},
96: {'menor': [REDUCE, 28], 'suma': [REDUCE, 28], 'coma': [REDUCE, 28], 'puntoycoma': [REDUCE, 28], 'parentesiscerrado': [REDUCE, 28], 'EOF': [REDUCE, 28]},
97: {'puntoycoma': [DESPLAZA, 99]},
98: {'if': [REDUCE, 15], 'let': [REDUCE, 15], 'for': [REDUCE, 15], 'id': [REDUCE, 15], 'put': [REDUCE, 15], 'get': [REDUCE, 15], 'return': [REDUCE, 15], 'llavecerrada': [REDUCE, 15], 'function': [REDUCE, 15], 'EOF': [REDUCE, 15]},
99: {'if': [REDUCE, 13], 'let': [REDUCE, 13], 'for': [REDUCE, 13], 'id': [REDUCE, 13], 'put': [REDUCE, 13], 'get': [REDUCE, 13], 'return': [REDUCE, 13], 'llavecerrada': [REDUCE, 13], 'function': [REDUCE, 13], 'EOF': [REDUCE, 13]},
100: {'if': [REDUCE, 16], 'let': [REDUCE, 16], 'for': [REDUCE, 16], 'id': [REDUCE, 16], 'put': [REDUCE, 16], 'get': [REDUCE, 16], 'return': [REDUCE, 16], 'llavecerrada': [REDUCE, 16], 'function': [REDUCE, 16], 'EOF': [REDUCE, 16]},
101: {'menor': [REDUCE, 9], 'suma': [REDUCE, 9], 'coma': [REDUCE, 9], 'puntoycoma': [REDUCE, 9], 'parentesiscerrado': [REDUCE, 9], 'EOF': [REDUCE, 9]},
102: {'id': [DESPLAZA, 103]},
103: {'puntoycoma': [DESPLAZA, 104]},
104: {'if': [REDUCE, 50], 'let': [REDUCE, 50], 'for': [REDUCE, 50], 'id': [REDUCE, 50], 'put': [REDUCE, 50], 'get': [REDUCE, 50], 'return': [REDUCE, 50], 'llavecerrada': [REDUCE, 50], 'function': [REDUCE, 50], 'EOF': [REDUCE, 50]},
105: {'if': [REDUCE, 51], 'let': [REDUCE, 51], 'for': [REDUCE, 51], 'id': [REDUCE, 51], 'put': [REDUCE, 51], 'get': [REDUCE, 51], 'return': [REDUCE, 51], 'llavecerrada': [REDUCE, 51], 'function': [REDUCE, 51], 'EOF': [REDUCE, 51]}
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
    4: REGLA( 'B', ['if', 'parentesisabierto', 'E', 'parentesiscerrado', 'S']),
    5: REGLA( 'B', ['S']),
    6: REGLA( 'B', ['let', 'id', 'T', 'puntoycoma']),
    7: REGLA( 'B', ['for', 'parentesisabierto', 'Y', 'puntoycoma', 'E', 'puntoycoma', 'D', 'parentesiscerrado', 'llaveabierta', 'C', 'llavecerrada']),
    8: REGLA( 'Y', ['id', 'asignacion', 'E']),
    9: REGLA( 'D', ['Y']),
    10: REGLA( 'T', ['int']),
    11: REGLA( 'T', ['string']),
    12: REGLA( 'T', ['boolean']),
    13: REGLA( 'S', ['id', 'asignacion', 'E', 'puntoycoma']),
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
    30: REGLA( 'V', ['entero']),
    31: REGLA( 'V', ['cadena']),
    32: REGLA( 'V', ['true']),
    33: REGLA( 'V', ['false']),
    34: REGLA( 'D', ['autodecremento', 'id']),
    35: REGLA( 'L', ['E', 'Q']),
    36: REGLA( 'Q', ['coma', 'E', 'Q']),
    37: REGLA( 'Q', []),
    38: REGLA( 'F', ['F1', 'llaveabierta', 'C', 'llavecerrada']),
    39: REGLA( 'F1', ['F2', 'parentesisabierto', 'A', 'parentesiscerrado']),
    40: REGLA( 'F2', ['function', 'id', 'H']),
    41: REGLA( 'H', ['T']),
    42: REGLA( 'H', ['void']),
    43: REGLA( 'H', []),
    44: REGLA( 'A', ['T', 'id', 'K']),
    45: REGLA( 'A', []),
    46: REGLA( 'K', ['coma', 'T', 'id', 'K']),
    47: REGLA( 'K', []),
    48: REGLA( 'C', ['B', 'C']),
    49: REGLA( 'C', []),
    50: REGLA( 'D1', ['autodecremento', 'id', 'puntoycoma']),
    51: REGLA( 'S', ['D1'])
    }
    
    def get_reglas():
        return Reglas.reglas

class AccionesSemanticas:

    def inicio(gestorTS, pila):
        pass

    def vacio(gestorTS, pila, regla_izquierda):
        pass
        
    def fin(gestorTS, pila, regla_izquierda):
        f = open("outputs/tablas.txt", "w")
        f.write(str(gestorTS))
        print(gestorTS)
        f.close()
    
    def asignacion(gestorTS, pila, regla_izquierda):
        regla_izquierda.tipo = pila[-2].tipo
        
    def asignacion_entera(gestorTS, pila, regla_izquierda):
        regla_izquierda.tipo = "entero"
    
    def let(gestorTS, pila, regla_izquierda):
        try:
            tabla = gestorTS.getActual()
            token = pila[-6]

            if tabla.get(token.valor) == None:
                tabla.add(tabladesimbolos.entradaTS(token.valor))

            tabla.get(token.valor)[0].tipo = pila[-4].tipo

            regla_izquierda.tipo = "ok"
    
        except:
            regla_izquierda.tipo = "error"
            raise Exception("Error semantico: el identificador " + token.lexema + " ya estaba declarada")
        
    def dar_valor_variable_con_puntoycoma(gestorTS, pila, regla_izquierda):
        try:
            # TODO : ¿Se puede acceder desde una funcion a una variable global? ¿Cómo se hace?
            tabla = gestorTS.getActual()
            E = pila[-4]
            id = pila[-8]
            if gestorTS.buscar(id.valor) == None:
                tabla.add(tabladesimbolos.entradaTS(id.valor))
            if gestorTS.buscar(id.valor)[0].tipo == E.tipo: #Cambio de valor
            
                regla_izquierda.tipo = "ok"
            elif gestorTS.buscar(id.valor)[0].tipo == None and E.tipo in ["entero", "cadena", "boolean"]: #Primera declaracion
                gestorTS.buscar(id.valor)[0].tipo = E.tipo
                regla_izquierda.tipo = "ok"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: no coinciden los tipos de la asignacion")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
        
    def dar_valor_variable_sin_puntoycoma(gestorTS, pila, regla_izquierda):
        try:
            tabla = gestorTS.getActual()
            E = pila[-2]
            token = pila[-6]
            if gestorTS.buscar(token.valor) == None:
                tabla.add(tabladesimbolos.entradaTS(token.valor))

            if gestorTS.buscar(token.valor)[0].tipo == E.tipo: #Cambio de valor
            
                regla_izquierda.tipo = "ok"
            elif gestorTS.buscar(token.valor)[0].tipo == None and E.tipo in ["entero", "cadena", "boolean"]: #Primera declaracion
                gestorTS.buscar(token.valor)[0].tipo = E.tipo
                regla_izquierda.tipo = "ok"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: no coinciden los tipos de la asignacion")

        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    
    def asignacion_id(gestorTS, pila, regla_izquierda):
        try:
            id = pila[-2]
            regla_izquierda.tipo = gestorTS.buscar(id.valor)[0].tipo
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    
    def bloque_if(gestorTS, pila, regla_izquierda):
        try:
            E = pila[-6]
            S = pila[-2]
            if E.tipo == "boolean":
                regla_izquierda.tipo = S.tipo
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: la expresion del if no es booleana")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    
    def asignacion_booleana(gestorTS, pila, regla_izquierda):
        regla_izquierda.tipo = "boolean"
    
    def asignacion_cadema(gestorTS, pila, regla_izquierda):
        regla_izquierda.tipo = "cadena"

    def menor_que(gestorTS, pila, regla_izquierda):
        try:
            U = pila[-2]
            R1 = pila[-6]
            if U.tipo == R1.tipo and U.tipo == "entero":
                regla_izquierda.tipo = "boolean"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: no coinciden los tipos de la comparacion")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    
    def autodecremento(gestorTS, pila, regla_izquierda):
        try:
            tabla = gestorTS.getActual()
            id = pila[-2]
            if tabla.get(id.valor)[0].tipo == "entero":
                regla_izquierda.tipo = "entero"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: el tipo de la variable no es entero")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    def suma(gestorTS, pila, regla_izquierda):
        try:
            V = pila[-2]
            U = pila[-6]
            if U.tipo == V.tipo and U.tipo == "entero":
                regla_izquierda.tipo = "entero"
            elif U.tipo == None or V.tipo == None:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: variable no declarada")
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: se deben sumar enteros")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e

    def comprobar_error_dos_simbolos(gestorTS, pila, regla_izquierda):
        try:
            C = pila[-2]
            B = pila[-4]
            if C.tipo == "error" or B.tipo == "error":
                regla_izquierda.tipo = "error"
            elif C.tipo == "ok" and B.tipo == "ok":
                regla_izquierda.tipo = "ok" #Entendemos por ok si no hay return (void)
            elif C.tipo in ["entero", "cadena", "boolean"] and B.tipo in ["entero", "cadena", "boolean"]:
                raise Exception("Error semantico: hay varios returns")
            elif C.tipo == "ok" and B.tipo in ["entero", "cadena", "boolean"]:
                regla_izquierda.tipo = B.tipo
            elif C.tipo in ["entero", "cadena", "boolean"] and B.tipo == "ok":
                regla_izquierda.tipo = C.tipo
    

        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
            
    def bloque_for(gestorTS, pila, regla_izquierda):
        try:
            C = pila [-4]
            D = pila[-10]
            E = pila[-14]
            Y = pila[-18]
            if Y.tipo != "error" and E.tipo == "boolean" and D.tipo != "error" and C.tipo == "ok":
                regla_izquierda.tipo = "ok"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: el for tiene errores")
        except:
            regla_izquierda.tipo = "error"
            raise Exception("Error semantico desconocido")
        
    def asignacion_void(gestorTS, pila, regla_izquierda):
        regla_izquierda.tipo = "void"

    def declaracion_funcion(gestorTS, pila, regla_izquierda):
        try:
            # TODO: Asegurarse de que no este tb en la TS Global
            gestorTS.getGlobal().add(tabladesimbolos.entradaTS(pila[-4].valor, tipo =  pila[-6].tipo, tipoRetorno = pila[-2].tipo, numParam=0, tipoParam=[]))
            gestorTS.add(pila[-4].valor)
            regla_izquierda.tipo = pila[-2].tipo
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    def creacion_funcion(gestorTS, pila, regla_izquierda):
        try:
            A = pila[-4]
            F2 = pila[-8]
            if A.tipo == "ok" and F2.tipo in ["entero", "boolean", "cadena", "void"]:
                regla_izquierda.tipo = "ok"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: la funcion tiene errores")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
        

        
    def argumento_funcion(gestorTS, pila, regla_izquierda):
        try:
            tabla = gestorTS.getActual()
            K = pila[-2]
            T = pila[-6]
            id = pila[-4]

            if tabla.get(id.valor) == None:
                tabla.add(tabladesimbolos.entradaTS(id.valor))
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: variable ya declarada")

            if (tabla.get(id.valor)[0].tipo == None and T.tipo in ["entero", "cadena", "boolean"]):
                tabla.get(id.valor)[0].tipo = T.tipo
                gestorTS.getGlobal().getUltimaEntrada().numParam += 1
                gestorTS.getGlobal().getUltimaEntrada().tipoParam.insert(0, T.tipo)
                regla_izquierda.tipo = "ok"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: variable ya declarada")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    
    def fin_funcion(gestorTS, pila, regla_izquierda):
        try:
            C = pila[-4]
            F1 = pila[-8]
            nombre_funcion = gestorTS.getActual().nombre
            tipo_retorno = gestorTS.getGlobal().get(nombre_funcion)[0].tipoRetorno
            tipo_retorno = "ok" if C.tipo == "void" else tipo_retorno
            if  F1.tipo == "ok":
                if tipo_retorno == C.tipo:
                    regla_izquierda.tipo = "ok"
                    gestorTS.cambiarGlobal()
                    tabla = gestorTS.getActual()
                elif C.tipo == "ok":
                    regla_izquierda.tipo = "error"
                    raise Exception("Error semantico: la funcion requiere retorno y no hay retorno")
                else:
                    regla_izquierda.tipo = "error"
                    raise Exception("Error semantico: la funcion tiene errores")
                    
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: la funcion tiene errores en su cabecera")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    def siguiente_argumento(gestorTS, pila, regla_izquierda):
        try:
            tabla = gestorTS.getActual()
            K = pila[-2]
            id = pila[-4]
            T = pila[-6]

            if tabla.get(id.valor) == None:
                tabla.add(tabladesimbolos.entradaTS(id.valor))
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: variable ya declarada")
            


            if (tabla.get(id.valor)[0].tipo == None and T.tipo in ["entero", "cadena", "boolean"]):
                tabla.get(id.valor)[0].tipo = T.tipo
                gestorTS.getGlobal().getUltimaEntrada().numParam += 1
                gestorTS.getGlobal().getUltimaEntrada().tipoParam.insert(0, T.tipo)
                regla_izquierda.tipo = "ok"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: variable ya declarada")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
        
    def llamar_funcion_muchos_argumentos(gestorTS, pila, regla_izquierda):
        try:
            tabla = gestorTS.getActual()
            E = pila[-4]
            Q = pila[-2]
            if (E.tipo in ["entero", "cadena", "boolean"]) and (Q.tipo == None or Q.tipo == "ok"):
                regla_izquierda.tipo = "ok"
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    
    def llamar_funcion_final_argumentos(gestorTS, pila, regla_izquierda):
        try:
            tabla = gestorTS.getActual()
            E = pila[-4]
            Q = pila[-2]
            if E.tipo == "void" and Q.tipo == None:
                regla_izquierda.tipo = "ok"
            else:
                AccionesSemanticas.llamar_funcion_muchos_argumentos(gestorTS, pila, regla_izquierda)
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    def fin_llamada_funcion(gestorTS, pila, regla_izquierda):
        try:
            id = pila[-10]
            L = pila[-6]
            if (L.tipo == "ok") and gestorTS.buscar(id.valor)[0].tipo == "function":
                regla_izquierda.tipo = gestorTS.buscar(id.valor)[0].tipoRetorno
                # regla_izquierda.tipo = "ok"
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: la funcion no existe")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
    def fin_llamada_funcion_sin_puntoycoma(gestorTS, pila, regla_izquierda):
        try:
            id = pila[-8]
            L = pila[-4]
            if (L.tipo == "ok") and gestorTS.buscar(id.valor)[0].tipo == "function":
                regla_izquierda.tipo = gestorTS.buscar(id.valor)[0].tipoRetorno
            else:
                regla_izquierda.tipo = "error"
                raise Exception("Error semantico: la funcion no existe")
        except Exception as e:
            regla_izquierda.tipo = "error"
            raise e
        
    
    diccionario_acciones_semanticas = {
        0: inicio,
        1: vacio,
        2: vacio,
        3: fin,
        4: bloque_if,
        5: asignacion,
        6: let,
        7: bloque_for,
        8: dar_valor_variable_sin_puntoycoma,
        9: asignacion,
        10: asignacion_entera,
        11: asignacion_cadema,
        12: asignacion_booleana,
        13: dar_valor_variable_con_puntoycoma,
        14: fin_llamada_funcion,

        18: asignacion,

        20: asignacion,
        21: menor_que,

        23: asignacion,
        24: suma,
        25: asignacion,

        27: asignacion_id,
        29:fin_llamada_funcion_sin_puntoycoma,
        30: asignacion_entera,
        31: asignacion_cadema,
        32: asignacion_booleana,
        33: asignacion_booleana,
        34: autodecremento,
        35: llamar_funcion_final_argumentos,
        36: llamar_funcion_muchos_argumentos,
        37: vacio,
        38: fin_funcion,
        39: creacion_funcion,
        40: declaracion_funcion,
        41: asignacion,
        42: asignacion_void,

        44:argumento_funcion,

        46: siguiente_argumento,
        47: vacio,
        48: comprobar_error_dos_simbolos,
        49: asignacion,
    }
    def get_accion(accion):
        try:
            return AccionesSemanticas.diccionario_acciones_semanticas[accion]
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    AccionesSemanticas.diccionario_acciones_semanticas[1]()