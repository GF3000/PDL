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

