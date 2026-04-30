r=0
area=0
a=0
volumen=0
def volumen_area():
    print('ingrese la altura de su cilindro')
    a=int(input())
    print('ingrese la radio de su cilindro')
    r=int(input())
    area=3.14*(r**2)
    volumen=3.1416*((r**2)*a)
    print('el volumen de su cilindro es: ',volumen)
    print('El area de su circulo es',area)
volumen_area()

