nombre = "birome"
precio = 1250.5
stock = 20
activo = True

if activo and stock > 0:
    print(f"{nombre} está disponible.")
else:
    print("Producto no disponible.")