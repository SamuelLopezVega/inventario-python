# Matriz del inventario
inventario = [
    [1, "Arroz", 10, 20],
    [2, "Azucar", 30, 25],
    [3, "Cafe", 5, 15],
    [4, "Leche", 50, 40],
    [5, "Pan", 8, 10]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
    return cantidad


# Recorrer la matriz
for producto in inventario:
    codigo = producto[0]
    nombre = producto[1]
    stock_actual = producto[2]
    stock_minimo = producto[3]

    # Llamar la función
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultados
    print("Código:", codigo)
    print("Producto:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock minimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("-----------------------------")
    
    input("Pulse Cualquier tecla para cerrar")
    
    