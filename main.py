#Archivo correspondiente al main del proyecto
import lexer
import tokens
import syntax
import tablas


def analizar(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    codigo = archivo.read()
    archivo.close()

    print("\nAnalizador Ascedendente LR(1)\n")

    print("\nSOURCE\n----------\n")
    print(codigo)
    print("\n----------\nEND SOURCE\n")

    print("\nANALISIS\n----------\n")

    #Se crea el objeto lexer
    tokens_lenguaje = tokens.Tokens.get_tokens()
    mi_lexer = lexer.Lexer(tokens_lenguaje)
    #Se analiza el código fuente
    try:
        tokens_analizados, gestor_TS = mi_lexer.analizar(codigo)
    except Exception as e:
        print(e)
        return False
  
    #Se crea el objeto syntax
    tabla_GOTO = tablas.Tabla_GOTO.get_tabla_GOTO()
    tabla_ACCION = tablas.Tabla_ACCION.get_tabla_ACCION()

    try:
        reglas = tablas.Reglas.get_reglas()
        mi_syntax = syntax.Syntax(tabla_GOTO, tabla_ACCION, reglas, imprimir =True, gestor_TS=gestor_TS)
        exito = mi_syntax.analizar(tokens_analizados)
    except Exception as e:
        print(e)
        exito = False

    print("\n----------\nEND ANALISIS\n")

    return exito


def main():

    exito = analizar("casosPruebaTxt/draco1.txt")
    print("[+] El analisis ha finalizado con exito" if  exito else "[-] El analisis ha finalizado con errores")

if __name__ == "__main__":
    main()