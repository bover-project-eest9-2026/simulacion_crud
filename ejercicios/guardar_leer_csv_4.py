from crud_basico_3 import agregar_producto
import csv

# guardar
def guardar_productos(productos, archivo):
    with open(archivo, mode='w', newline='') as f:
        writer= csv.DictWriter(f, fieldnames=productos[0].keys())
        writer.writeheader()
        writer.writerows(productos)

# leer
def leer_productos(archivo):
    with open(archivo, mode='r') as f:
        reader= csv.DictReader(f)
        return list(reader)



# Ejemplo de uso
lista_productos = []

# Cargas productos usando la función importada
agregar_producto(lista_productos, "birome", 1250.5, 20, True)
agregar_producto(lista_productos, "lapiz", 1000, 20, True)

# Guardas en archivo CSV
guardar_productos(lista_productos, "productos.csv")

# Lees el archivo CSV
productos_guardados = leer_productos("productos.csv")
print(productos_guardados)