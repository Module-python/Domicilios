# Inicio
print("PEDIDO DE PIZZA\n")

# Validación: ¿Pido Pizza?
while True:
    pedir = input("¿Pido Pizza? (si/no): ").lower()
    if pedir == "si" or pedir == "no":
        break
    print(" Error: Escribe 'si' o 'no'\n")

if pedir == "si":
    # Validación: Hago Pedido
    while True:
        print("\nPizzas: 1.Margarita $10  2.Pepperoni $12")
        pizza = input("Elige (1 o 2): ")
        if pizza == "1" or pizza == "2":
            break
        print("Error: Escribe '1' o '2'\n")
    
    # Validación: Acepto Precio
    while True:
        acepto = input("¿Acepta precio? (si/no): ").lower()
        if acepto == "si" or acepto == "no":
            break
        print("Error: Escribe 'si' o 'no'\n")
    
    if acepto == "si":
        # Confirmo y Pago
        print("\n✓ Confirmando pedido...")
        print("✓ Pago realizado")
        
        # Espero Entrega
        print("✓ Pizza en camino...")
        
        # Validación: Pedido Correcto
        while True:
            correcto = input("¿Pedido correcto? (si/no): ").lower()
            if correcto == "si" or correcto == "no":
                break
            print("Error: Escribe 'si' o 'no'\n")
        
        if correcto == "si":
            print("\n ¡Disfruta tu pizza!")
        else:
            # Reclamo
            print("✓ Enviando nueva pizza gratis")
            print("\n¡Disfruta tu pizza!")
    else:
        print("\n↩️ Vuelve a elegir otro día")

# Fin
print("\n¡Hasta pronto!")