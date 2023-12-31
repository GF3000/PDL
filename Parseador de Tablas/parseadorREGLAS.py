#read reglas.txt

with open('Parseador de Tablas/reglas.txt', 'r') as f:
    reglas = f.readlines()

contador = 1

for regla in reglas:
    linea = regla.split(' ')
    #Remove = "" from each element
    linea[-1] = linea[-1][:-1]
    for elemento in linea:
        if len(elemento) == 0:
            linea.remove(elemento)
        if elemento == 'lambda':
            linea.remove(elemento)
            li
    
    print(f"{contador}: REGLA( '{linea[0]}', {linea[2:]}),")
    with open('Parseador de Tablas/reglas_dict.txt', 'a') as f:
        f.write(f"{contador}: REGLA( '{linea[0]}', {linea[2:]}),\n")
    contador += 1