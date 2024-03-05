# -*- coding: utf-8 -*-
"""Actividad 3 Datos Copiados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gTB5-XvyghzIuWjj1UzAE3iuUaZm-wtz
"""

pip install matplotlib

from matplotlib import pyplot as plt

import numpy as np

plt.style.use("fivethirtyeight")
#MOSTRAR ESTO COMO UN GRÁFICO DE BARRAS
#Salario medio de los desarrolladores por edad
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200, 56000,
         62316, 64928, 67317, 68748, 73752]

plt.bar(x_indexes - width, dev_y, width=width, color='#4ab0d4', linestyle='--', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65988,
            70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width=width, color='#493e63', label='Python')


#Salario medio de Desarrolladores en JavaScript por edad
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375,
            66674, 68745, 68746, 74583]

plt.bar(x_indexes + width, js_dev_y, width=width, color='#ffd700', label='JavaScript')

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age', color='#493e63')

plt.legend()

plt.tight_layout()

#plt.savefig('plot.png')

plt.show()