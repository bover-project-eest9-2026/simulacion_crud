productos = [
    {
        "id": 1,
        "nombre":"Birome",
        "precio": 1250.5,
        "stock": 20,
        "activo": True
        },
    {
        "id":2,
        "nombre":"Lapiz 2H",
        "precio": 1000,
        "stock": 15,
        "activo": True
        },
    {
        "id": 3,
        "nombre": "Boligoma",
        "precio": 2000,
        "stock": 10,
        "activo": True
        },
    {
        "id": 4,
        "nombre": "Tijeras",
        "precio": 2500,
        "stock": 5,
        "activo": True
        }
]

for producto in productos:
    if producto["activo"] and producto["stock"] > 0:
        print(f"{producto["nombre"]} - ${producto["precio"]} - {producto['stock']} unidades disponibles.")
