import logging
logging.basicConfig(filename='log_contable.log', level=logging.ERROR)
from librodiario import LibroDiario
libro = LibroDiario()
#libro.agregar_transaccion('18/06/2025', 'Compra de laptop', 780, 'egreso')
#libro.agregar_transaccion('18/06/2025', 'Venta de sensor TK-110', 780, 'Ingreso')
#libro.agregar_transaccion('18/06/2025', 'Compra de insumos de oficina', -85.60, 'egreso')

try:
    libro.cargar_transacciones_desde_archivo("datos.csv")
##print(libro.calcular_resumen())
    libro.exportar_resumen("resumen.txt")
except Exception as e:
    logging.exception(f"Error no controlado en el flujo principal: {e}")
    print("Error.")
finally:
    print("Programa finalizado.")