"""Verifica los requisitos y evita que duplicados alteren los datos."""
import subprocess
import sys
import unittest
from pathlib import Path

from main import (analizar_prestamos, buscar_libro, catalogo_ordenado,
                  datos_ejemplo, registrar_libro, registrar_prestamo,
                  registrar_socio, socio_registrado)


class BibliotecaTest(unittest.TestCase):
    def test_catalogo_y_duplicados(self):
        catalogo, _, _ = datos_ejemplo()
        original = catalogo['L001'].copy()
        self.assertFalse(registrar_libro(catalogo, 'L001', 'Otro', 'Otro'))
        self.assertEqual(buscar_libro(catalogo, 'L001'), original)
        self.assertIsNone(buscar_libro(catalogo, 'NO'))
        self.assertTrue(registrar_libro(catalogo, 'L004', 'Cosmos', 'Carl Sagan'))
        self.assertEqual([c for c, _ in catalogo_ordenado(catalogo)],
                         ['L001', 'L002', 'L003', 'L004'])

    def test_socios_y_prestamos(self):
        _, socios, prestamos = datos_ejemplo()
        self.assertFalse(registrar_socio(socios, 'S001'))
        self.assertEqual(len(socios), 4)
        self.assertTrue(registrar_socio(socios, 'S005'))
        self.assertTrue(socio_registrado(socios, 'S005'))
        self.assertFalse(registrar_prestamo(socios, prestamos, 'NO', 'novela'))
        self.assertFalse(registrar_prestamo(socios, prestamos, 'S001', 'otro'))
        self.assertTrue(registrar_prestamo(socios, prestamos, 'S001', 'novela'))
        self.assertEqual(len(prestamos['novela']), 2)

    def test_operaciones(self):
        _, _, prestamos = datos_ejemplo()
        self.assertEqual(analizar_prestamos(prestamos['novela'], prestamos['ciencia']),
                         ({'S002'}, {'S001'}, {'S001', 'S002', 'S003'}))
        self.assertEqual(analizar_prestamos(set(), set()), (set(), set(), set()))
        self.assertEqual(analizar_prestamos({'A'}, set()), (set(), {'A'}, {'A'}))

    def test_menu(self):
        resultado = subprocess.run([sys.executable, 'main.py'],
                                  cwd=Path(__file__).parent,
                                  input='3\n7\n9\n0\n', text=True,
                                  capture_output=True, check=True)
        self.assertIn('Total: 3', resultado.stdout)
        self.assertIn('Hasta pronto.', resultado.stdout)


if __name__ == '__main__':
    unittest.main()
