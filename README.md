# PDL


## Diseño  

Existen 4 clases a día de hoy (12/10):

-tokens.py: Contiene los tokens configuarados como en Draco. Se almacenan como  {token, atributo, expresion regular} siendo la expreiosn regular la encargada de encontrarlos  
-lexer.py: Clase principal del analizador léxico. Se instancia con los tokens y devuelve una lista con los tokens analizados.  
-entradaTS.py: Representa cada entrada (fila) de la Tabla de Simbolos. Contiene el método toString (__str__ en python)  
-tabladesimbolos.py: Clase principal de la tabla de símbolos. El método "add_identifier" es el que se encarga de añadir una nueva entrada  

## Por hacer  

-Queda mucho trabajo que hacer en la tabla de símbolos. Hay qué entender bien qué se pide y qué tenemos hecho.  
-Integración de la TS con el lexer. Cuando se añade una nueva variable no sabemos qué desplazamiento hay que usar. Ahora mismo el desplazamiento está autoincrementado una unidad por entrada pero no es correcto (creo)
