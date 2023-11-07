class syntaxAnalyzer:

    def __init__(self, grammar, first, follow):
        self.grammar = grammar
        self.first = first
        self.follow = follow

    # Función para calcular el conjunto FIRST para un símbolo no terminal
    def calculate_first(self, symbol):
        # Si el símbolo es terminal, el conjunto FIRST es el mismo símbolo
        if symbol not in self.grammar:
            return {symbol}

        # Si el conjunto FIRST ya ha sido calculado, devolverlo, evitando así bucles infinitos
        if symbol in first:
            return first[symbol]

        # Crear un conjunto vacío para el conjunto FIRST del símbolo no terminal
        first_set = set()

        # Obtener las producciones del símbolo no terminal
        productions = grammar[symbol]

        # Iterar sobre todas las producciones
        for production in productions:
            if len(production) == 0:  # Producción vacía
                first_set.add('')
            else: # Producción no vacía
                for simbolo_en_produccion in production:
                    if (simbolo_en_produccion in grammar) and ('' in self.calculate_first(simbolo_en_produccion)): # Símbolo no terminal con símbolo vacío en su conjunto FIRST
                        first_set.update(self.calculate_first(simbolo_en_produccion)) # Calcular el conjunto FIRST del símbolo no terminal
                        #Continuar con el siguiente símbolo en la producción
                    else:
                        first_set.update(self.calculate_first(simbolo_en_produccion)) # Calcular el conjunto FIRST del símbolo no terminal
                        break # Detener el ciclo

        first[symbol] = first_set # Guardar el conjunto FIRST calculado para el símbolo no terminal
        return first_set

    # Función para calcular el conjunto FOLLOW para un símbolo no terminal
    def calculate_follow(self, symbol):

        # Si el conjunto FOLLOW ya ha sido calculado, devolverlo, evitando así bucles infinitos
        if symbol in follow:
            return follow[symbol]

        # Crear un conjunto vacío para el conjunto FOLLOW del símbolo no terminal
        follow_set = set()

        # El símbolo inicial tiene '$' en su conjunto FOLLOW
        if symbol == 'S':
            follow_set.add('$')  # El símbolo de fin de entrada

        # Iterar sobre todas las producciones
        for no_terminal in grammar:
            producciones = grammar[no_terminal] # Obtener las producciones del símbolo no terminal
            for produccion in producciones: #Iterar sobre todas las producciones
                for i, simbolo_en_produccion in enumerate(produccion): #Iterar sobre todos los símbolos de la producción
                    if simbolo_en_produccion == symbol: # Símbolo encontrado en la producción
                        if i == len(produccion) - 1:  # Símbolo en la posición final de la producción
                            if no_terminal != symbol: # Evitar bucles infinitos
                                follow_set.update(self.calculate_follow(no_terminal)) # Calcular el conjunto FOLLOW del símbolo no terminal
                        else:
                            first_siguiente = self.calculate_first(produccion[i + 1]) # Calcular el conjunto FIRST del siguiente símbolo
                            if '' in first_siguiente: # Símbolo vacío en el conjunto FIRST del siguiente símbolo
                                follow_set.update(self.calculate_follow(no_terminal)) # Calcular el conjunto FOLLOW del símbolo no terminal
                                follow_set.update(first_siguiente - {''})   # Calcular el conjunto FIRST del siguiente símbolo
                            else: # Símbolo vacío no encontrado en el conjunto FIRST del siguiente símbolo
                                follow_set.update(first_siguiente) # Calcular el conjunto FIRST del siguiente símbolo

        follow[symbol] = follow_set # Guardar el conjunto FOLLOW calculado para el símbolo no terminal
        return follow_set
    
    def print_first(self):
        for symbol in grammar:
            print(f"FIRST({symbol}) = {first[symbol]}")

    def print_follow(self):
        for symbol in grammar:
            print(f"FOLLOW({symbol}) = {follow[symbol]}")
    
    def print_grammar(self):
        for symbol in grammar:
            print(f"{symbol} -> {grammar[symbol]}")

    def parse(tokens, grammar, start_symbol, first_sets, follow_sets):
        #Falta implementar
        pass

if __name__ == "__main__":

    # Definir la gramática
    grammar1 = {
        'S': [['A'], ['B']],
        'A': [['a', 'A'], []],
        'B': [['b', 'B'], []]
    }

    grammar2 = {
        'S': [['T', 'V'], ['V', 'Z']],
        'T': [['a', 'T'], ['b', 'T'], ['h']],
        'V': [[], ['c', 'Z', 'h']],
        'Z': [[], ['d', 'Z']]
    }

    # Seleccionar la gramática a utilizar
    grammar = grammar2

    # Conjuntos FIRST y FOLLOW iniciales vacíos
    first = {}
    follow = {}

    # Crear un objeto de la clase syntaxAnalyzer
    miAnalizador = syntaxAnalyzer(grammar, first, follow)
    
    # Calcular los conjuntos FIRST y FOLLOW para todos los símbolos no terminales
    for non_terminal in grammar:
        miAnalizador.calculate_first(non_terminal)
        miAnalizador.calculate_follow(non_terminal)

    # Imprimir los conjuntos FIRST y FOLLOW
    print("Gramática:")
    miAnalizador.print_grammar()
    print("\nFIRST:")
    miAnalizador.print_first()
    print("\nFOLLOW:")
    miAnalizador.print_follow()
    
