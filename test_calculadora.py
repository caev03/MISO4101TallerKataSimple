from unittest import TestCase

import Calculadora

class TestCalculadora(TestCase):
    def test_procesar(self):
        self.assertEqual(Calculadora.Calculadora().procesar(""),[0,"","",""], "Cadena Vacia")

    def test_procesar_numero(self):
	self.assertEqual([1,1,1,1],Calculadora.Calculadora().procesar("1"),"Un numero")
