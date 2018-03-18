from unittest import TestCase

import Calculadora

class TestCalculadora(TestCase):
    def test_procesar(self):
        self.assertEqual(Calculadora.Calculadora().procesar(""),"[0,"","",""]", "Cadena Vacia")
