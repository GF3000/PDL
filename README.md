# PDL


## Diseño  

Existen 4 clases a día de hoy (12/10):

-tokens.py: Contiene los tokens configuarados como en Draco. Se almacenan como  {token, atributo, expresion regular} siendo la expreiosn regular la encargada de encontrarlos  
-lexer.py: Clase principal del analizador léxico. Se instancia con los tokens y devuelve una lista con los tokens analizados.  
-entradaTS.py: Representa cada entrada (fila) de la Tabla de Simbolos. Contiene el método toString (__str__ en python)  
-tabladesimbolos.py: Clase principal de la tabla de símbolos. El método "add_identifier" es el que se encarga de añadir una nueva entrada  

## Por hacer  

-- Tabla de simbolos
    Dejo en temporal.py el codigo que estaba implementado en TS, porque resulta que el analizador lexico solo tiene que añadir los lexemas de los ID que encuentre, y estaba programando lo que tenia que hacer el analizador semantico. Lo dejo ahi para reutilizarlo proximamente.

    El gestor.py es una idea para que desde ahi se lleve el control de las tablas y subtablas, y se encargue de eliminarlas depsues. Aun no lo he implementado
