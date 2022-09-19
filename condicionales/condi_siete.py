# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

menu = """
Tenemos dos tipos de piza

1 - Vegetariana: Pimiento y tofu.
2 - No vegetarianos: Peperoni, Jamón y Salmón

Eligue una opción: """

opcion = input(menu)

if opcion == '1':
    print("Elegiste Pizza vegetariana.")
    ingredites_extras= input("Vas elegir un ingrediente extra - SI [1] - NO [2]: ")
    if ingredites_extras == '1':
        extras = """
        Que ingrediente extra le vas agregar a tu pizza vegetariana

        1 - Piña.
        2 - Brocoli.
        3 - Esparragos.

        Elige una opción: """
        elige_ingrediente_extra = input(extras)
        if elige_ingrediente_extra == '1':
            print("Tu pizza vegetariana con mozzarell, tomate y piña ya estan lista. Gracias por su compra.")

        elif elige_ingrediente_extra == '2':
            print("Tu pizza vegetariana con mozzarell, tomate y brocoli ya estan lista. Gracias por su compra.")

        elif elige_ingrediente_extra == '3':
            print("Tu pizza vegetariana con mozzarell, tomate y esparragos ya estan lista. Gracias por su compra.")
        
        else:
            print("Debes elegir una opcion correcta.")

    elif ingredites_extras == '2':
        print("Tu pizza vegetariana con mozzarell Y tomate ya estan lista. Gracias por su compra.")

    else:
        print("Debes elegir una opcion correcta.")
            
elif opcion == '2':
    print("Elegiste Pizza no vegetariana.")
    ingredites_extras= input("Vas elegir un ingrediente extra - SI [1] - NO [2]: ")
    if ingredites_extras == '1':
        extras = """
        Que ingrediente extra le vas agregar a tu pizza vegetariana

        1 - Pollo.
        2 - Carne.
        3 - Biste.

        Elige una opción: """
        elige_ingrediente_extra = input(extras)
        if elige_ingrediente_extra == '1':
            print("Tu pizza vegetariana con mozzarell, tomate y pollo ya estan lista. Gracias por su compra.")

        elif elige_ingrediente_extra == '2':
            print("Tu pizza vegetariana con mozzarell, tomate y carne ya estan lista. Gracias por su compra.")

        elif elige_ingrediente_extra == '3':
            print("Tu pizza vegetariana con mozzarell, tomate y biste ya estan lista. Gracias por su compra.")
        
        else:
            print("Debes elegir una opcion correcta.")

    elif ingredites_extras == 2:
        print("Tu pizza vegetariana con mozzarell Y tomate ya estan lista. Gracias por su compra.")

    else:
        print("Debes elegir una opcion correcta.")
        
else:
        print("Debes elegir una opcion correcta.")