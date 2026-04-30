
def conversor():
    celsius = float(input("Ingrese grados Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print('los',celsius,'°C en fahrenheit es: ',fahrenheit,'°f')
conversor()
def conversor2():
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(fahrenheit,'°f en celsius es: ',celsius,'°C')
conversor2()