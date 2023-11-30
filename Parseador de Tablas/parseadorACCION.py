#Read csv
# -*- coding: utf-8 -*-
import csv

with open('ACCION.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

nombres_columnas = "if	let	for	=	int	boolean	string	id	put	get	return	<	!	+	entero	cadena	true	false	--	,	;	{	}	(	)	void	function	$"
nombres_columnas = nombres_columnas.split('\t')
filas = your_list[1:]
for fila in filas:
    cadena = ""
    #split fila using ;
    fila[0].split(';')
    nueva_fila = fila[0].split(';')
    estado = nueva_fila[0]
    nueva_fila = nueva_fila[1:]
    for index, celda in enumerate(nueva_fila):
        texto_celda = ""
        if celda != '':
            if celda[0] == 'r':
                texto_celda = "REDUCE" + ", "+ celda[1:]
            elif celda[0] == 'd':
                texto_celda = "DESPLAZA" + ", "+ celda[1:]
            else:
                texto_celda = "EXITO, None"
            cadena = cadena + "'"+ nombres_columnas[index] + "': ["+ texto_celda + "], "
    #Remove last comma
    cadena = cadena[:-2]
    print(estado + ": {" + cadena + "},")
    with open('ACCION_dict.txt', 'a') as f:
        f.write(estado + ": {" + cadena + "},\n")


# print(nombres_columnas)