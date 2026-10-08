class Producto:
    def __init__(self, id, nombre, precio, stock, activo):
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.activo=activo
    def mostrar(self):
        print(f"{self.nombre} - ${self.precio} (Stock: {self.stock})")


if __name__ == "__main__":
    # LAS INSTANCIAS
    p1 = Producto(1, "birome", 1250.5, 20, True)
    p2 = Producto(2, "lapiz", 1000, 15, True)

    # METODO MOSTRAR
    p1.mostrar()
    p2.mostrar()

    # RECORRIENDO LISTA
    productos = [p1, p2]
    print("\n--- Recorriendo la lista ---")
    for prod in productos:
        prod.mostrar()