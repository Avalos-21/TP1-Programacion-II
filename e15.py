from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

aux=0

imagen= Image.open("pandaRojo")
gris= imagen.convert("L")

m=np.array(gris)
fil, col =m.shape
for i in range(fil):
    for j in range(col//2):
        ind_op=col-1-j
        aux=m[i][j]
        m[i][j]= m[i][ind_op]
        m[i][ind_op]=aux

plt.imshow(m, cmap="gray")
plt.show()

gris= m.convert("L")
plt.imshow(imagen, cmap="gray")
plt.show()

