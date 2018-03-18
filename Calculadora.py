__author__ = 'caev03'

class Calculadora:

	def procesar(self, cadena):
		if(len(cadena) == 0):
			return [0,"","",""]
		elif(len(cadena) == 1):
			valor = int(cadena)
			return [1, valor, valor, valor]
		elif(len(cadena) == 3):
			valorU = int(cadena[0])
			valorD = int(cadena[2])
			return [2,min(valorU,valorD),max(valorU,valorD),(valorU+valorD)/2]
		return [3,1,3,2]
