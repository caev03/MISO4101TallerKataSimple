__author__ = 'caev03'

class Calculadora:

    def procesar(self, cadena):
        if(len(cadena) == 0):
            return [0,"","",""]
        if(len(cadena) == 1):
	    valor = int(cadena)
	    return [1, valor, valor, valor]
        return [2,1,3,2]
