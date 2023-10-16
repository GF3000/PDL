# PDL


## Diseño  

Existen 4 clases a día de hoy (12/10):

-tokens.py: Contiene los tokens configuarados como en Draco. Se almacenan como  {token, atributo, expresion regular} siendo la expreiosn regular la encargada de encontrarlos  
-lexer.py: Clase principal del analizador léxico. Se instancia con los tokens y devuelve una lista con los tokens analizados.  
-entradaTS.py: Representa cada entrada (fila) de la Tabla de Simbolos. Contiene el método toString (__str__ en python)  
-tabladesimbolos.py: Clase principal de la tabla de símbolos. El método "add_identifier" es el que se encarga de añadir una nueva entrada  

## Por hacer  

-- Tabla de simbolos
    He metido la imagen ejemplo_visual_tabla para que sea mas facil visualizarlo

    Hay comentarios de lo que queda por hacer tanto en el lexer.py como en la tabladesimbolos.py
    
    Hay que centrarse en las subtablas de funciones y corregir tema desplazamientos y que se metan entradas a la tabla cuanto variables no vienen declaradas con el tipo delante. p.ej int x, o x = 0; la x deberia estar en la tabla de simbolos y aún no está implementado
    P.ej: i.txt funciona bien, pero si usamos entrada.txt, ya entran funciones y aún no está implementado

    El gestor.py es una idea para que desde ahi se lleve el control de las tablas y subtablas, y se encargue de eliminarlas depsues
