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
		else:
			valores = cadena.split(",")
			miin = int(valores[0])
			maax = int(valores[0])
			promedio = 0
			for num in valores:
				nume = int(num)
				promedio = promedio + nume
				if nume<miin:
					miin = nume
				if nume>maax:
					maax = nume
			return [len(valores), miin, maax, promedio/len(valores)]
		return ["","","",""]
