class OrderedSet:
    """Implementación de un conjunto ordenado"""

    def __init__(self, iterable=None):
        self.data = []
        self.set_data = set()
        if iterable is not None:
            self.update(iterable)

    def add(self, item):
        """Añade un elemento al conjunto"""
        if item not in self.set_data:
            self.data.append(item)
            self.set_data.add(item)
            self.order() #Para que el elemento vacío siempre esté al final

    def update(self, iterable):
        """Añade los elementos de un iterable al conjunto"""
        for item in iterable:
            self.add(item)

    def remove(self, item):
        """Elimina un elemento del conjunto"""
        if item in self.set_data:
            self.data.remove(item)
            self.set_data.remove(item)

    def discard(self, item):
        """Elimina un elemento del conjunto si está presente"""
        if item in self.set_data:
            self.data.remove(item)
            self.set_data.discard(item)

    def clear(self):
        """Elimina todos los elementos del conjunto"""
        self.data = []
        self.set_data = set()

    def order(self):
        """Ordena el conjunto colocando el elemento vacío al final"""

        if ("" in self.set_data):
            self.data.remove("")
            self.data.append("")
        return self.data
    
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

    def __and__(self, other):
        if isinstance(other, OrderedSet) or isinstance(other, set):
            new_ordered_set = OrderedSet()
            for item in self:
                if item in other:
                    new_ordered_set.add(item)
            return new_ordered_set
        else:
            raise TypeError("Unsupported operand type for &: 'OrderedSet' and {}".format(type(other)))
    
    def __xor__(self, other):
        if isinstance(other, OrderedSet) or isinstance(other, set):
            new_ordered_set = OrderedSet()
            for item in self:
                if item not in other:
                    new_ordered_set.add(item)
            for item in other:
                if item not in self:
                    new_ordered_set.add(item)
            return new_ordered_set
        else:
            raise TypeError("Unsupported operand type for ^: 'OrderedSet' and {}".format(type(other)))

    def __or__(self, other):
        if isinstance(other, OrderedSet) or isinstance(other, set):
            new_ordered_set = OrderedSet(self.data)
            new_ordered_set.update(other)
            return new_ordered_set
        else:
            raise TypeError("Unsupported operand type for |: 'OrderedSet' and {}".format(type(other)))
    