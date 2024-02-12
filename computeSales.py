"""Module ayuda a poder utilizar
la funcion json, sys y time para
ejecutar el programa."""  # pylint: disable=invalid-name
import json
import sys
import time

# Verificando archivos JSON como argumentos
if len(sys.argv) < 3 or len(sys.argv) % 2 != 1:
    print("Agregar los archivoss JSON requeridos como argumentos.")
    sys.exit(1)

# Iterando en archivos JSON
for i in range(2, len(sys.argv)):
    archivo_actual = sys.argv[i]

    if "Sales" in archivo_actual:
        productos_file_name = sys.argv[1]
        ventas_file_name = archivo_actual
        try:
            with open(productos_file_name, 'r', encoding="utf-8") as productos_file:  # noqa: E501
                productos_data = json.load(productos_file)
            with open(ventas_file_name, 'r', encoding="utf-8") as ventas_file:
                ventas_data = json.load(ventas_file)
            productos_dict = {producto['title']: producto for producto in productos_data}  # noqa: E501  # pylint: disable=line-too-long
            start_time = time.time()
            TOTAL_COST = 0
            resultados_str = f"\n{ventas_file_name}:\n"
            for venta in ventas_data:
                producto_nombre = venta['Product']
                cantidad = venta['Quantity']
                if producto_nombre in productos_dict:
                    producto = productos_dict[producto_nombre]
                    costo_total = producto['price'] * cantidad
                    venta['Costo_Total'] = costo_total
                    TOTAL_COST += costo_total
                else:
                    print(f"Error en {ventas_file_name}: Producto '{producto_nombre}' no encontrado.")  # pylint: disable=line-too-long  # noqa: E501
            resultados_str += f"Precio Total de Ventas: ${TOTAL_COST:.2f}\n"
            end_time = time.time()
            processing_time = end_time - start_time
            resultados_str += f"Tiempo de Procesamiento: {processing_time:.4f} segundos\n"  # noqa: E501 # pylint: disable=line-too-long
            print(resultados_str)
            with open('SalesResults.txt', 'a', encoding="utf-8") as resultados_file:  # noqa: E501
                resultados_file.write(resultados_str)
        except ImportError as e:
            print(f"Error al procesar {ventas_file_name}: {str(e)}")

print("Resultados guardados en SalesResults.txt")
