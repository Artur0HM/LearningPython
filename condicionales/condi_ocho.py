# Un comerciante compra un artículo a un costo dado. Determine el precio al cual debe venderlo si desea ganar el 15%.

compra_del_articulo = float(input("Ingrese el costo del articulo: "))
porcentaje = int(input("Ingresa el porcentaje de ganancia: "))

print("El articulo que compraste consto", compra_del_articulo , "dolares.")
print("Debes ganar el", porcentaje ,"%")

ganancia = compra_del_articulo * porcentaje / 100

print("Para ganar el", porcentaje , "% deberas de aumentar el precio en", ganancia)
print("Para ganar el", porcentaje , "% deberas venderlo a", ganancia + compra_del_articulo , "dolares.")

