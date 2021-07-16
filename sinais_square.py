import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from scipy import signal as si

n = np.arange(0,48)
yD1 = si.square(pi/8*n)
#criando os gráficos
fig, ax = plt.subplots(1,1)
ax.stem(n, yD1, linefmt='b-',use_line_collection=True)
ax.set_xlabel("Amostras")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.set_title('y[n] = Square(n*pi/8)')
fig.tight_layout()
plt.show()