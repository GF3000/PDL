#Archivo correspondiente al main del proyecto
import lexer
import tokens
import syntax
import tablas



def main():
    #Se abre el archivo de entrada
    archivo = open("casosPruebaTxt/casoPrueba2.txt", "r")
    #Se lee el archivo
    codigo = archivo.read()
    #Se cierra el archivo
    archivo.close()

    print("Analizando:\n")
    print(codigo)

    #Se crea el objeto lexer
    tokens_lenguaje = tokens.Tokens.get_tokens()
    mi_lexer = lexer.Lexer(tokens_lenguaje)
    #Se analiza el código fuente
    tokens_analizados = mi_lexer.analizar(codigo)

    #Se crea el objeto syntax
    tabla_GOTO = tablas.Tabla_GOTO.get_tabla_GOTO()
    tabla_ACCION = tablas.Tabla_ACCION.get_tabla_ACCION()
    reglas = tablas.Reglas.get_reglas()
    mi_syntax = syntax.Syntax(tabla_GOTO, tabla_ACCION, reglas, impresion=True)

    #Se analizan los tokens
    tokens_procesados = []
    for token in tokens_analizados:
        tokens_procesados.append(token.token_type)
    print(tokens_procesados)
    print("\n\n")
    exito = mi_syntax.analizar(tokens_procesados)

    print("\n\n")
    print("[+] El analisis ha finalizado con exito" if  exito else "[-] El analisis ha finalizado con errores")

if __name__ == "__main__":
    main()