import unittest
from calculadora import dividir


class TestCalculadora(unittest.TestCase):

    def test_divisao_exata(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_decimal(self):
        self.assertEqual(dividir(5, 2), 2.5)

    def test_divisao_com_negativo(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_zero_dividido_por_numero(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)
