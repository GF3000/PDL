#Archivo correspondiente al main del proyecto
import analizadorLR1
import gramatica
import tabladesimbolos
import analizadorLR1


# Funcion que analiza el archivo pasado como parametro
# Se usa para hacer las pruebas por consola

def analizar_pruebas(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    codigo = archivo.read()
    archivo.close()

    print("\nAnalizador Ascedendente LR(1)\n")

    print("\nSOURCE\n----------\n")
    print(codigo)
    print("\n----------\nEND SOURCE\n")

    print("\nANALISIS\n----------\n")

   
    tabla_GOTO = gramatica.Tabla_GOTO.get_tabla_GOTO()
    tabla_ACCION = gramatica.Tabla_ACCION.get_tabla_ACCION()
    reglas = gramatica.Reglas.get_reglas()
    mi_syntax = analizadorLR1.AnalizadorLR1(tabla_GOTO, tabla_ACCION, reglas, imprimir =True, gestor_TS=tabladesimbolos.gestorTablas())
    try:
        exito = mi_syntax.analizar(nombre_archivo)
    except Exception as e:
        print(e)
        exito = False

    print("\n----------\nEND ANALISIS\n")

    return exito


# Funcion que analiza el archivo pasado como parametro
# Se usa para la interfaz grafica
def analizar_gui(nombre_archivo):
    tabla_GOTO = gramatica.Tabla_GOTO.get_tabla_GOTO()
    tabla_ACCION = gramatica.Tabla_ACCION.get_tabla_ACCION()
    reglas = gramatica.Reglas.get_reglas()
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