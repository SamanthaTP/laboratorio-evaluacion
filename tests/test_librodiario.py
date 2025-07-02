import unittest
from librodiario import LibroDiario, Montoerror

class TestLibroDiario(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.libro = LibroDiario()

    def test_creacion_instancia(self):
        """Verifica que se cree correctamente una instancia de LibroDiario."""
        self.assertIsInstance(self.libro, LibroDiario)
        self.assertEqual(self.libro.transacciones, [])

    def test_agregar_transaccion_valida(self):
        """Verifica que una transacción válida se agregue correctamente."""
        self.libro.agregar_transaccion("2025-07-01", "Venta de producto", 100.50, "ingreso")
        self.assertEqual(len(self.libro.transacciones), 1)
        self.assertEqual(self.libro.transacciones[0]["descripcion"], "Venta de producto")
        self.assertEqual(self.libro.transacciones[0]["monto"], 100.50)

    def test_agregar_transaccion_monto_negativo(self):
        """Verifica que no se agregue la transacción si el monto es negativo."""
        self.libro.agregar_transaccion("2025-07-01", "Compra inválida", -50.0, "egreso")
        self.assertEqual(len(self.libro.transacciones), 0)


    def test_agregar_transaccion_tipo_invalido(self):
        self.libro.agregar_transaccion("2025-07-01", "Tipo inválido", 100.0, "gasto")
        self.assertEqual(len(self.libro.transacciones), 0)


    def test_calcular_resumen_formato(self):
        """Verifica que el resumen tenga las claves y valores correctos."""
        self.libro.agregar_transaccion("2025-07-01", "Ingreso válido", 100.0, "ingreso")
        self.libro.agregar_transaccion("2025-07-01", "Egreso válido", 40.0, "egreso")
        resumen = self.libro.calcular_resumen()
        self.assertIn("ingresos", resumen)
        self.assertIn("egresos", resumen)
        self.assertIsInstance(resumen["ingresos"], float)
        self.assertIsInstance(resumen["egresos"], float)
        self.assertEqual(resumen["ingresos"], 100.0)
        self.assertEqual(resumen["egresos"], 40.0)

    def test_cargar_transacciones_desde_archivo(self):
        """
        Verifica que al cargar el archivo datos.csv:
        - Solo se agregue 1 transacción válida.
        - Las demás (con montos negativos) se ignoren.
        """
        self.libro.cargar_transacciones_desde_archivo("datos.csv")
        resumen = self.libro.calcular_resumen()

        # Solo una transacción debe ser válida (la primera)
        self.assertEqual(len(self.libro.transacciones), 1)
        self.assertAlmostEqual(resumen["ingresos"], 2500.0)
        self.assertAlmostEqual(resumen["egresos"], 0.0)

if __name__ == "__main__":
    unittest.main()

