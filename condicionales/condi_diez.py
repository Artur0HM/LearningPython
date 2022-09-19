# En un almacén se rebaja 10% del precio al cliente si compra mas de 20 artículos y 5% si compra hasta 20 artículos pero más de 10. Dado el precio unitario de un artículo y la cantidad adquirida, muestre lo que debe pagar el cliente .

cantidad_de_productos = int(input("Cantidad de productos comprados: "))
precio_del_pructo = 25
primer_descuento = 10
segundo_descuento = 5

if cantidad_de_productos > 20:
    print("la cantidad del productos es de", cantidad_de_productos)
    print("cada uno tiene un valor de", precio_del_pructo , "dolares." )
    print("tiemes un descuento del", primer_descuento , "%")
    print("Total a pagar es de:",((cantidad_de_productos * precio_del_pructo) - (precio_del_pructo * cantidad_de_productos) * primer_descuento / 100), "dolares")

# elif cantidad_de_productos >= 10 and cantidad_de_productos <= 20:
#     print("la cantidad del productos es de", cantidad_de_productos)
#     print("cada uno tiene un valor de", precio_del_pructo , "dolares." )
#     print("tiemes un descuento del", segundo_descuento , "%")
#     print("Total a pagar es de:",((cantidad_de_productos * precio_del_pructo) - (precio_del_pructo * cantidad_de_productos) * segundo_descuento / 100), "dolares")

else:
    print("la cantidad del productos es de", cantidad_de_productos)
    print("cada uno tiene un valor de", precio_del_pructo , "dolares." )
    print("tiemes un descuento del", segundo_descuento , "%")
    print("Total a pagar es de:",((cantidad_de_productos * precio_del_pructo) - (precio_del_pructo * cantidad_de_productos) * segundo_descuento / 100), "dolares")
