from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

imagen= Image.open("panda.png").convert("L")
m=np.array(imagen)
n= m.shape[0]
op=int(input("1-Izquierda 2-Derecha 3-180:"))

rotar= np.zeros(m.shape, dtype=int)

for i in range(n):
    for j in range(n):
        if op==1:
            rotar[n-1-j,i]=m[i,j]
        elif op==2:
            rotar[j,n-1-i]=m[i,j]
        else:
            rotar[n-1-i,n-1-i]=m[i,j]
           
plt.imshow(rotar,cmap="gray")            
plt.axis("off")
plt.show()
        
        
        
        