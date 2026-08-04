def conversor():
    print(" Conversor de sistema de Numeracion y ASCII ")
    print(" 1: Decimal,\n 2: Binario,\n 3: Hexadecimal,\n 4: ASCII")
    
    origen = input("Elija el sistema actual: ")
    valor = input("Ingresa el numero a convertir: ")
    destino = input("Elige el sistema de destino(1-4): ")

    if origen == '1':
        decimal = int(valor)
    elif origen == '2':
        decimal = int(valor, 2)
    elif origen == '3':
        decimal = int(valor, 16)
    elif origen == '4':
        decimal = ord(valor)
    else:
        print("Origen no válido")

    
    if destino == '1':
        resultado = str(decimal)
    elif destino == '2':
        resultado = bin(decimal)[2:]
    elif destino == '3':
        resultado = hex(decimal)[2:].upper() 
    elif destino == '4':
        resultado = chr(decimal)
    else:
        print( "Destino no válido")

    print(f"Resultado: {resultado}")
conversor()

