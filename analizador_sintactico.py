class OrderedSet:
    """Implementación de un conjunto ordenado"""

    def __init__(self, iterable=None):
        self.data = []
        self.set_data = set()
        if iterable is not None:
            self.update(iterable)

    def add(self, item):
        if item not in self.set_data:
            self.data.append(item)
            self.set_data.add(item)

    def update(self, iterable):
        for item in iterable:
            self.add(item)

    def remove(self, item):
        if item in self.set_data:
            self.data.remove(item)
            self.set_data.remove(item)

    def discard(self, item):
        if item in self.set_data:
            self.data.remove(item)
            self.set_data.discard(item)

    def clear(self):
        self.data = []
        self.set_data = set()

    def __contains__(self, item):
        return item in self.set_data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return repr(self.data)
    
    def __sub__(self, other):
        if isinstance(other, OrderedSet) or isinstance(other, set):
            new_ordered_set = OrderedSet(self.data)
            for item in other:
                new_ordered_set.discard(item)
            return new_ordered_set
        else:
            raise TypeError("Unsupported operand type for -: 'OrderedSet' and {}".format(type(other)))


        



class syntaxAnalyzer:

    def __init__(self, grammar, first = None, follow = None):
        if follow is None:
            follow = {}
        if first is None:
            first = {}
        self.grammar = grammar
        self.first = first
        self.follow = follow

    # Función para calcular el conjunto FIRST para un símbolo no terminal
    def calculate_first(self, symbol):
        # Si el símbolo es terminal, el conjunto FIRST es el mismo símbolo
        if symbol not in self.grammar:
            return {symbol}

        # Si el conjunto FIRST ya ha sido calculado, devolverlo, evitando así bucles infinitos
        if symbol in self.first:
            return self.first[symbol]

        # Crear un conjunto vacío para el conjunto FIRST del símbolo no terminal
        first_set = OrderedSet()

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
                        print(f"FIRST({symbol}) = {first_set}")
                        #Continuar con el siguiente símbolo en la producción
                    else:
                        first_set.update(self.calculate_first(simbolo_en_produccion)) # Calcular el conjunto FIRST del símbolo no terminal
                        print(f"FIRST({symbol}) = {first_set}")
                        break # Detener el ciclo

        self.first[symbol] = first_set # Guardar el conjunto FIRST calculado para el símbolo no terminal
        return first_set

    # Función para calcular el conjunto FOLLOW para un símbolo no terminal
    def calculate_follow(self, symbol):

        # Si el conjunto FOLLOW ya ha sido calculado, devolverlo, evitando así bucles infinitos
        if symbol in self.follow:
            return self.follow[symbol]

        # Crear un conjunto vacío para el conjunto FOLLOW del símbolo no terminal
        follow_set = OrderedSet()

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

        self.follow[symbol] = follow_set # Guardar el conjunto FOLLOW calculado para el símbolo no terminal
        return follow_set
    
    def print_first(self):
        for symbol in grammar:
            print(f"FIRST({symbol}) = {self.first[symbol]}")

    def print_follow(self):
        for symbol in grammar:
            print(f"FOLLOW({symbol}) = {self.follow[symbol]}")
    
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

    # Crear un objeto de la clase syntaxAnalyzer
    miAnalizador = syntaxAnalyzer(grammar)
    
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
    
