# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:39:29 2023

@author: Adri
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5] # coordenadas x
y = [6,7,8,9,10] # coordenadas y

plt.scatter(x, y,color='red',s=100,marker='*')
plt.plot(x,y,color='blue',label='grafico de lineas') # label siempre funciona con legend
plt.xlabel('AXIS-X')
plt.ylabel('AXIS-Y')
plt.title('SCATTERPLOT')
plt.grid(True)
plt.legend()

# Histograma

data = [1,1,1,2,3,3,3,4,4,4,5,5,6,6,7,7,7,7,8,8,8,9]
plt.hist(data,color='red',alpha=0.5,bins=5)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histograma')
plt.grid(False)

# Dos histogramas
import numpy as np

variable1 = np.random.normal(0,1,1000)
variable2 = np.random.normal(2,1,1000)

plt.hist(variable1,alpha=0.5,bins=20,label='Variable 1')
plt.hist(variable2,alpha=0.5,bins=20, label='Variable 2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histograma')


# Barplots

x = ['Categoria 1','Categoria 2','Categoria 3','Categoria 4']
y = [15,20,12,8]
plt.bar(x,y,color='Skyblue',width=0.5)
plt.xticks(rotation=45)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Grafico de barras')


# Barplots horizontal

x = ['Categoria 1','Categoria 2','Categoria 3','Categoria 4']
y = [15,20,12,8]

plt.barh(x,y,color='Skyblue')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Grafico de barras')

# Barplots horizontal con distintos colores

x = ['Categoria 1','Categoria 2','Categoria 3','Categoria 4']
y = [15,20,12,8]

plt.barh(x,y,color=(['b','r','g','m']))
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Grafico de barras')


#Grafico de tarta

size = [30,20,15,10,25]
labelss = ['Categoria 1','Categoria 2','Categoria 3','Categoria 4','Categoria 5']
colores = ['#1c61f2','#45ec26','#c3e458','#b81346','#36fde3']
plt.pie(size,labels=labelss,autopct='%1.1f%%',explode=[0,0.1,0,0.2,0.5],colors=colores)


