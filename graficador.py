import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

vec=np.loadtxt('datos.txt',usecols=0)

Z=np.zeros(shape=(101,601))

    
for i in range(601):
    Z[:,i]=vec[i*101:(i+1)*101]
    
  
X=np.array(range(101))/101
T=6*np.array(range(601))/601
T,X=np.meshgrid(T,X)
plt.figure()
ax = plt.gca(projection='3d')
surf = ax.plot_surface(T, X, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.1, 1.11)
plt.colorbar(surf, shrink=0.5, aspect=10)
plt.savefig('graficas.png')

