def tienda_de_ropa():
    # Lista de productos 
    productos = [
        {'nombre': 'Camiseta', 'precio': 15.50, 'stock': 10},
        {'nombre': 'Pantalón', 'precio': 29.50, 'stock': 5},
        {'nombre': 'Chaqueta', 'precio': 49.59, 'stock': 2},
        {'nombre': 'Zapatos', 'precio': 39.60, 'stock': 7}
    ]
    
    # Aplicar un descuento > 30 productos
    for producto in productos:          #p1
        if producto['precio'] > 30:     #P2
            producto['precio'] *= 0.10  
        else:                           
            continue  # Sino continua    #p3
    
    # Para ver si aun hay producto disponible
    def verificar_disponibilidad(producto_nombre):      #p4
        for producto in productos:
            if producto['nombre'] == producto_nombre:   #p5
                if producto['stock'] > 0:               
                    return True
                else:
                    return False                        #p6
        return False  # Si no encuentra el producto     #P7
    
    # Simulación
    carrito = []
    while True:                                         #P8
        producto_nombre = input("Ingrese el nombre del producto que desea comprar (o 'salir' para finalizar): ")
        if producto_nombre.lower() == 'salir':          #P9
            break
        
        if verificar_disponibilidad(producto_nombre):       #p10
            for producto in productos:                      
                if producto['nombre'] == producto_nombre:   #p11
                    carrito.append(producto)                #p12
                    producto['stock'] -= 1  # Reducir el stock          
                    print(f"{producto_nombre} añadido al carrito.")
                    break                                   
        else:
            print("Producto no disponible o fuera de stock.")   #p13
    
    # Calcular el total de la compra
    total = 0
    for item in carrito:
        total += item['precio']
    
    print(f"Total a pagar: ${total:.2f}")
    
    return total                                        #F


total_pagar = tienda_de_ropa()
print(f"Total final: ${total_pagar:.2f}")
