class entradaTS:
    def __init__(self, lexema, tipo = None, desplazamiento = 0,
                  numParam = None, tipoParam = None,
                    tipoRetorno = None):
        self.lexema = lexema
        self.tipo = tipo
        self.desplazamiento = desplazamiento
        self.numParam = numParam
        self.tipoParam = tipoParam if tipoParam else []
        self.tipoRetorno = tipoRetorno
    def __str__(self):
        devolucion = ""
        devolucion += f"* LEXEMA : \'{self.lexema}\'\n"
        devolucion += f"\t+ tipo : \'{self.tipo}\'\n"
        if self.tipo != "function":
            devolucion += f"\t+ desplazamiento : {self.desplazamiento}\n"
        if self.numParam:
            devolucion += f"\t+ numParam : {self.numParam}\n"
        if self.tipoParam:
            for i in range(len(self.tipoParam)):
                devolucion += f"\t+ tipoParam{i} : \'{self.tipoParam[i]}\'\n"
        if self.tipoRetorno:
            devolucion += f"\t+ tipoRetorno : \'{self.tipoRetorno}\'\n"
        return devolucion
    
        
        
        
        

class tabladesimbolos:
    def __init__(self, numero,  entradas = None) -> None:
        self.numero = numero
        self.entradas = entradas if entradas else []
    def __str__(self) -> str:
        devolucion = ""
        devolucion += f"Tabla #{self.numero}:\n"
        for entrada in self.entradas:
            devolucion += str(entrada)
        return devolucion
    
    def add(self, entrada):
        entrada.desplazamiento = self.getHueco()
        self.entradas.append(entrada)
        return self.entradas.index(entrada)

    def get(self, lexema):
        for entrada in self.entradas:
            if entrada.lexema == lexema:
                return entrada, self.entradas.index(entrada)
        return None
    def getHueco(self):
        if not self.entradas:
            return 0
        tipo = self.entradas[-1].tipo
        if tipo == "entero":
            return self.entradas[-1].desplazamiento + 1
        elif tipo == "cadena":
            return self.entradas[-1].desplazamiento + 64
        elif tipo == "boolean":
            return self.entradas[-1].desplazamiento + 1
        elif tipo == "function":
            return self.entradas[-1].desplazamiento + 0
        else:
            return self.entradas[-1].desplazamiento + 0

class gestorTablas:
    def __init__(self) -> None:
        self.tablas = []
        self.tablas.append(tabladesimbolos(1))
        self.tablaActual = 1
    def __str__(self) -> str:
        devolucion = ""
        for tabla in self.tablas:
            devolucion += str(tabla)
            devolucion += "\n"
        return devolucion
    
    def add(self):
        tabla = tabladesimbolos(len(self.tablas) + 1)
        self.tablas.append(tabla)
        self.tablaActual = len(self.tablas)
        return tabla

    def getActual(self):
        return self.tablas[self.tablaActual - 1]
    
    def getGlobal(self):
        return self.tablas[0]
    
    def cambiarGlobal(self):
        self.tablaActual = 1

    

def main():

    entradas = []
    entradas.append(entradaTS("a", tipo = "entero"))
    entradas.append(entradaTS("b", tipo = "entero"))
    entradas.append(entradaTS("suma", tipo = "function", numParam=2, tipoParam=["entero", "entero"], tipoRetorno="entero"))
    entradas.append(entradaTS("resta", tipo = "function", numParam=2, tipoParam=["entero", "entero"], tipoRetorno="entero"))
    entradas.append(entradaTS("c", tipo = "entero"))
    mi_gestorTablas = gestorTablas()
    tablaGlobal = mi_gestorTablas.getActual()
    for entrada in entradas:
        tablaGlobal.add(entrada)
    tablaLocal = mi_gestorTablas.add()
    tablaLocal.add(entradaTS("d", tipo = "entero"))
    tablaLocal.add(entradaTS("e", tipo = "entero"))
    tablaLocal.add(entradaTS("f", tipo = "entero"))
    tablaLocal.add(entradaTS("g", tipo = "entero"))
    tablaLocal.add(entradaTS("multiplicacion", tipo = "function", numParam=2, tipoParam=["entero", "entero"], tipoRetorno="entero"))
    print(mi_gestorTablas)

if __name__ == "__main__":
    main()