#Read csv
# -*- coding: utf-8 -*-
import csv

with open('Parseador de Tablas/GOTO.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

your_list = your_list[1:]
nombres_columnas = "P	B	Y	T	S	X	E	R	U	V	D	L	Q	F	F1	F2	H	A	K	C"
nombres_columnas = nombres_columnas.split('\t')

for fila in your_list:
    impresion = ""
    fila = fila[0].split(';')
    estado = fila[0]
    #Check if estado is a number
    impresion += estado + ": {"
    for elemento in fila[1:]:
        if elemento != '':
            impresion += "'"+ nombres_columnas[(fila[1:].index(elemento))] + "': " + elemento + ","
    impresion = impresion[:-1]
    impresion += "},"
    if (len(impresion) > 10):
        #If file GOTO_dict.txt  exists, it will be overwritten
        with open('Parseador de Tablas/GOTO_dict.txt', 'a') as f:
            f.write(impresion + "\n")
        print(impresion)
