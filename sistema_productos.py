import csv

# 1:
archivo = "productos.csv"

# 2: 
def mostrar_productos(lista):
    if not lista:
        print("No hay productos cargados.")
        return
    print("\n=== LISTA DE PRODUCTOS ===")
    for p in lista:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']} - Stock: {p['stock']} - Activo: {p['activo']}")

def agregar_producto(lista):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    activo = True
    
    nuevo = {
        "id": len(lista) + 1,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": activo
    }
    lista.append(nuevo)
    print(f"Producto '{nombre}' agregado con éxito.")

def modificar_stock(lista):
    mostrar_productos(lista)
    try:
        id_prod = int(input("Ingrese el ID del producto a modificar: "))
        nuevo_stock = int(input("Nuevo stock: "))
        for p in lista:
            if p["id"] == id_prod:
                p["stock"] = nuevo_stock
                print("Stock actualizado correctamente.")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Error: ID o valor de stock inválido.")

def eliminar_producto(lista):
    mostrar_productos(lista)
    try:
        id_prod = int(input("Ingrese el ID del producto a eliminar: "))
        for p in lista:
            if p["id"] == id_prod:
                p["activo"] = False
                print(f"Producto '{p['nombre']}' dado de baja.")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Error: ID inválido.")

# 3:
def guardar_productos(lista, archivo):
    with open(archivo, mode='w', newline='') as f:
        campos = ["id", "nombre", "precio", "stock", "activo"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)

def leer_productos(archivo):
    try:
        with open(archivo, mode='r') as f:
            reader = csv.DictReader(f)
            productos = list(reader)
            # Convertir tipos de datos
            for p in productos:
                p["id"] = int(p["id"])
                p["precio"] = float(p["precio"])
                p["stock"] = int(p["stock"])
                p["activo"] = p["activo"].lower() == "true"
            return productos
    except FileNotFoundError:
        return []

# 4:
def menu():
    print("\n=== SISTEMA DE PRODUCTOS ===")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Modificar stock")
    print("4. Eliminar producto")
    print("5. Guardar y salir")

# 5:
def main():
    productos = leer_productos(archivo)
    while True:
        menu()
        opcion = input("Elija una opción: ")
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(productos)
        elif opcion == "3":
            modificar_stock(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            guardar_productos(productos, archivo)
            print("Datos guardados. Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()