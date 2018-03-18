from unittest import TestCase

import Calculadora

class TestCalculadora(TestCase):
    def test_procesar(self):
        self.assertEqual(Calculadora.Calculadora().procesar(""),[0,"","",""], "Cadena Vacia")

    def test_procesar_numero(self):
        self.assertEqual([1,1,1,1],Calculadora.Calculadora().procesar("1"),"Un numero")

    def test_procesar_dos_numeros(self):
        self.assertEqual([2,1,3,2],Calculadora.Calculadora().procesar("1,3"),"Dos Numeros")

    def test_procesar_cadena(self):
        self.assertEqual([3,1,3,2],Calculadora.Calculadora().procesar("1,2,3"),"Cadena")
