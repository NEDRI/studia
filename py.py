import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3*np.pi, 3*np.pi, 0.5)
y = np.arange(-3*np.pi, 3*np.pi, 0.5)
X, Y = np.meshgrid(x, y)
Z = 600 - X * Y + 50 * np.sin(X) + 50 * np.sin(Y)

fig = plt.figure(figsize=(12, 10))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_wireframe(X, Y, Z)
ax1.set_title('Wykres siatkowy')

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(X, Y, Z)
ax2.set_title('Wykres powierzchniowy')

ax3 = fig.add_subplot(2, 2, 3)
ax3.contourf(X, Y, Z)
ax3.set_title('Wykres warstwicowy')

ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot_wireframe(X, Y, Z)
ax4.contour(X, Y, Z, zdir='z', offset=Z.min())
ax4.set_title('Wykres siatkowy z warstwicami')

plt.tight_layout()
plt.show()