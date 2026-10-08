lista = list()
def agregar_producto(lista, nombre, precio, stock, activo):
    nuevo_id = len(lista) + 1
    producto = {
    "id": nuevo_id,
    "nombre": nombre,
    "precio": precio,
    "stock": stock,
    "activo": activo
    }
    lista.append(producto)

agregar_producto(lista, "birome", 1250.5, 20, True)
agregar_producto(lista, "lapiz", 1000, 20, True)
agregar_producto(lista, "tijera", 2500, 20, True)
agregar_producto(lista, "goma", 300, 20, True)

def mostrar_lista(lista):
    for producto in lista:
        print(f"""
            ============================
            ID: {producto["id"]}
            NOMBRE: {producto["nombre"]}
            PRECIO: {producto["precio"]}
            STOCK: {producto["stock"]}
            ACTIVO: {producto["activo"]}
            ============================
        """)