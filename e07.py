from datetime import datetime, timezone
dia=0
mes=0
año=0
fecha=0
edadD=0
edadA=0
print('Ingrese el dia de su nacimiento')
dia=int(input())
print('ingrese el mes de su nacimiento')
mes=int(input())
print('ingrese el año de su nacimiento')
año=int(input())
ahora=datetime.now()#fecha actual
fecha=datetime(año,mes,dia)
edadD=ahora-fecha
print('su edad es dias y horas es:',edadD)
edadA=edadD.days//365#.days da solo los días como número, #//365 da un numero entero
print('su edad es:',edadA,'años')
