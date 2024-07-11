import numpy as np
from qiskit.visualization import plot_state_qsphere
import matplotlib.pyplot as plt

x = np.sqrt(1/2)
vec = (x*1, x*1)
print(vec)

# Asignar el gráfico a una variable
graph = plot_state_qsphere(vec)

# Mostrar el gráfico
plt.show()
