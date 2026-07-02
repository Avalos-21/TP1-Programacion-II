def resultado   
palabra=""
desplazamiento=0
alfabeto="abcdefghijklmnñopqrstvwxyz"
resultado=""
indice=0
indice_actual =0

print('Ingrese un texto para cifrar')
palabra=input()
print('Ingrese en cuanto quiere desplazar la letra')
desplazamiento=int(input())

for letra in palabra:
   if letra in alfabeto:
       indice=alfabeto.index(letra)
       nuevo_indice = (indice + desplazamiento) % len(alfabeto)
       resultado += alfabeto[nuevo_indice]
   else:
       resultado += letra
       
 return resultado    