cantex=0
mil=0
rest=0
dos=0
restos=0

print('ingrese la cantidad de dinero a extraer')
cantex=int(input())

mil=cantex//1000
rest=cantex%1000

dos=rest//200
restos=cantex%200

print(' cantidaad de billetes')
print('billetes de 1000 =',mil)
print('billetes de 200 =',dos)
