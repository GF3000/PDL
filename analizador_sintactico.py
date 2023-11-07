class syntaxAnalyzer:

    def __init__(self, grammar, first, follow):
        self.grammar = grammar
        self.first = first
        self.follow = follow

    # Función para calcular el conjunto FIRST para un símbolo no terminal
    def calculate_first(self, symbol):
        #Check if symbol is a terminal symbol
        if symbol not in self.grammar:
            return {symbol}

        if symbol in first:
            return first[symbol]

        first_set = set()
        productions = grammar[symbol]

        for production in productions:
            if len(production) == 0:  # Producción vacía
                first_set.add('')
            else:
                for i, symbol_in_production in enumerate(production):
                    if (production[i] in grammar) and ('' in self.calculate_first(production[i])):
                        first_set.update(self.calculate_first(production[i]) - {''})
                    else:
                        first_set.update(self.calculate_first(production[i]))
                        break
            # elif production[0] in grammar:  # Símbolo no terminal
            #     first_set.update(self.calculate_first(production[0]))
            # else:  # Símbolo terminal
            #     first_set.add(production[0])

        first[symbol] = first_set
        return first_set

    # Función para calcular el conjunto FOLLOW para un símbolo no terminal
    def calculate_follow(self, symbol):
        if symbol in follow:
            return follow[symbol]

        follow_set = set()

        if symbol == 'S':
            follow_set.add('$')  # El símbolo de fin de entrada

        for non_terminal in grammar:
            productions = grammar[non_terminal]
            for production in productions: #Iterar sobre todas las producciones
                for i, symbol_in_production in enumerate(production): #Iterar sobre todos los símbolos de la producción
                    if symbol_in_production == symbol: # Símbolo encontrado en la producción
                        if i == len(production) - 1:  # Símbolo en la posición final de la producción
                            if non_terminal != symbol: # Evitar bucles infinitos
                                follow_set.update(self.calculate_follow(non_terminal)) # Calcular el conjunto FOLLOW del símbolo no terminal
                        else:
                            first_of_next = self.calculate_first(production[i + 1])
                            if '' in first_of_next: # Símbolo vacío en el conjunto FIRST del siguiente símbolo
                                follow_set.update(self.calculate_follow(non_terminal))
                                follow_set.update(first_of_next - {''})
                            else:
                                follow_set.update(first_of_next)

        follow[symbol] = follow_set
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
    
