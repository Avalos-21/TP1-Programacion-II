cant=0
repartir=0
total=0
sobran=0
print('ingrese la cantidad de caramelos')
cant=int(input())

print('ingrese en cuantos lo quiere repartir')
repartir=int(input())

total=cant//repartir
sobran=cant%repartir

print('A cada alumno le corresponden',total)
print('le sobran',sobran,'caramelos')

