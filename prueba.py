name = input("¿Cómo te llamas? ")
ultima_letra = name[-1]
match ultima_letra:
    case "a" :
        print("Hola, mujer")
    case "e"| "u":
        print("Hola, hombre")
    case _:
        print("Hola, persone")