import math
f=0
r=0
def factorial_p():
    print('ingrese un numero para sacar el factorial')
    f=int(input())
    r=math.factorial(f)
    print('el factorial de',f,'es: ',r)
factorial_p()