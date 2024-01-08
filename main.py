#Archivo correspondiente al main del proyecto
import analizadorLR1
import tablas
import tabladesimbolos
import analizadorLR1


def analizar_pruebas(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    codigo = archivo.read()
    archivo.close()

    print("\nAnalizador Ascedendente LR(1)\n")

    print("\nSOURCE\n----------\n")
    print(codigo)
    print("\n----------\nEND SOURCE\n")

    print("\nANALISIS\n----------\n")

   
    tabla_GOTO = tablas.Tabla_GOTO.get_tabla_GOTO()
    tabla_ACCION = tablas.Tabla_ACCION.get_tabla_ACCION()
    reglas = tablas.Reglas.get_reglas()
    mi_syntax = analizadorLR1.AnalizadorLR1(tabla_GOTO, tabla_ACCION, reglas, imprimir =True, gestor_TS=tabladesimbolos.gestorTablas())
    try:
        exito = mi_syntax.analizar(nombre_archivo)
    except Exception as e:
        print(e)
        exito = False

    print("\n----------\nEND ANALISIS\n")

    return exito


def analizar_gui(nombre_archivo):
    tabla_GOTO = tablas.Tabla_GOTO.get_tabla_GOTO()
    tabla_ACCION = tablas.Tabla_ACCION.get_tabla_ACCION()
    reglas = tablas.Reglas.get_reglas()
    mi_syntax = analizadorLR1.AnalizadorLR1(tabla_GOTO, tabla_ACCION, reglas, imprimir =False, gestor_TS=tabladesimbolos.gestorTablas())

    try:
        exito = mi_syntax.analizar(nombre_archivo)
        if exito:
            return "[+] El analisis ha finalizado con exito", True
        else:
            return "[-] El analisis ha finalizado con errores", False
    except Exception as e:
        return (e), False
        


def main():

    exito = analizar_pruebas("in.txt")
    print("[+] El analisis ha finalizado con exito" if  exito else "[-] El analisis ha finalizado con errores")

if __name__ == "__main__":
    main()