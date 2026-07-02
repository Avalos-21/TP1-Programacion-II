from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

imagen= Image.open("panda.png")
imagen=np.array(imagen)
dimenciones=np.shape(imagen)
grises=np.zeros((dimenciones[0],dimenciones[1]))

for i in range(dimenciones[0]):
    for j in range(dimenciones[1]):
        grises[i][j]=(imagen[i][j][0]*0.2959+imagen[i][j][1]*0.5870+imagen[i][j][2]*0.1140)
                

plt.imshow(grises,cmap="gray")
plt.show()     