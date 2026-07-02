m=[[1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]]
sumad1=0
multid1=1
sumad2=0
multid2=1
for i in range(4):
    for j in range(4):
        if(i==j):
            sumad1=sumad1+m[i][i]
            multid1=multid1*m[i][i]
        if(i+j ==3):
            sumad2=sumad2+m[i][j]
            multid2=multid2*m[i][j]
  
print("el resultado de la suma de la diagonal es:",sumad1)
print("El resultado de  multiplicacion de la diagonal es:", multid1)
print("el resultado de la suma de la contra diagonal es:",sumad2)
print("El resultado de  multiplicacion de la contra diagonal es:", multid2)
