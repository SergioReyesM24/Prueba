import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('dataset.csv')
print(df.head())

# Hacer una gráfica con este dataset
plt.figure(figsize=(10, 6))
plt.plot(df['mes'], df['ventas'], marker='o', linestyle='-', color='b')
plt.title('Gráfica de ventas según el mes')

plt.savefig('grafica_x_vs_y.png')
plt.show()