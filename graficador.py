import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

vec=np.loadtxt('datos.txt',usecols=0)

Z=np.zeros(shape=(101,601))

    
for i in range(601):
    Z[:,i]=vec[i*101:(i+1)*101]

Y0=Z[:,0]
Yf=Z[:,-1]

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(1,2,1,projection='3d')
X=np.array(range(101))/101
T=6*np.array(range(601))/601
T,X=np.meshgrid(T,X)
surf = ax1.plot_surface(T, X, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.ylabel('Posición [metros]')
plt.xlabel('Tiempo [segundos]')
ax1.set_zlim(-1.1, 1.1)
fig.colorbar(surf, shrink=0.5, aspect=5)

X=np.array(range(101))/101
ax2=fig.add_subplot(1,2,2)
plt.plot(X, Y0, label='tiempo inicial')
plt.plot(X, Yf, label='tiempo final')
plt.ylabel('Desplazamiento [metros]')
plt.xlabel('Posición [metros]')
plt.legend()
plt.savefig('graficas.png')

