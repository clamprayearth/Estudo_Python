import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

n = np.arange(-10,11)
print(n)
yD1 = 2*np.cos(pi/4*n)
#criando os gráficos
fig, ax = plt.subplots(1,1)
ax.stem(n, yD1, linefmt='b-',use_line_collection=True)
ax.set_xlabel("Amostras")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.set_title('y[n] = 2cos(pi/4n)')
fig.tight_layout()
plt.show()