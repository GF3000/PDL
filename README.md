# PDL

Existen 4 clases a día de hoy (12/10):

-tokens.py: Contiene los tokens configuarados como en Draco. Se almacenan como  {token, atributo, expresion regular} siendo la expreiosn regular la encargada de encontrarlos
-lexer.py: Clase principal del analizador léxico. Se instancia con los tokens y devuelve una lista con los tokens analizados.
-entradaTS.py: Representa cada entrada (fila) de la Tabla de Simbolos. Contiene el método toString (__str__ en python)
-tabladesimbolos.py: Clase principal de la tabla de símbolos. El método "add_identifier" es el que se encarga de añadir una nueva entrada
