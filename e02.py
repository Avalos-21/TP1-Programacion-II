import random
numA=random.randint(1,20)
num=0
vidas=6
jugar=""
print('hola!! juguemos a las adivinanzas')
print('tienes',vidas,'intentos')
for x in range(1,7,1):
    print('ingresa un numero')
    num=int(input())
    if (num==numA):
        print('ADIVINASTE')
        
    else:
        vidas=vidas-1
        print('Ese no es el numero, te quedan',vidas,'vidas')
        
        if(num>numA):
            print('pista, el numero es menor al que ingresaste')
            
        else:
            print('pista, el numero es mayor al que ingresaste')
        
            
    
print(numA)

