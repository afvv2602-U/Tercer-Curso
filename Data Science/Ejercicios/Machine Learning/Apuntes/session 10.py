# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:56:58 2023

@author: Javi
"""


# =============================================================================
# ##~ Decima Clase
# =============================================================================

# =============================================================================
# ##~K-Means
# =============================================================================
#Carga de librerías.
import pandas as pd
from sklearn import preprocessing 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Carga del dataframe.
pokemon = pd.read_excel("pokemon.xlsx")
datoskmeans = pokemon.loc[:,["Attack","Defense"]]


#Se eliminan filas que tengan valor NaN.
datoskmeans = datoskmeans.dropna()
datoskmeans = datoskmeans.reset_index(drop=True)

#Normalización de los datos.
min_max_scaler = preprocessing.MinMaxScaler() 
datos_escalados = min_max_scaler.fit_transform(datoskmeans)
datos_escalados = pd.DataFrame(datos_escalados) # Hay que convertir a DF el resultado.
datos_escalados = datos_escalados.rename(columns = {0: 'Attack', 1: 'Defense'})

#Representación gráfica de los datos.
x = datos_escalados['Attack'].values
y = datos_escalados['Defense'].values
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack vs Speed')
plt.plot(x,y,'o',markersize=1)

#Curva elbow para determinar valor óptimo de k.
from plotnine import *
elbow_values = []
for i in range(1,11,1):
    km = KMeans(n_clusters=i)
    km.fit(datos_escalados)
    elbow_values.append(km.inertia_)
elbow = pd.DataFrame({"clusters":range(1,11,1), "elbow" : elbow_values})    
    
ggplot(aes(x = "clusters", y ="elbow"),elbow)+geom_line()+geom_point()+ggtitle("Elbow graph")

#Aplicación de k-means con k = 5.
kmeans = KMeans(n_clusters=5).fit(datos_escalados)
centroids = kmeans.cluster_centers_
print(centroids)

#Etiquetamos nuestro dataframe.
cluster = kmeans.predict(datos_escalados)
pokemon ["cluster"] = cluster

#Representación gráfica de los clústeres k-means.
colores=['red','green','blue','yellow','fuchsia']
asignar=[]
for row in cluster:
     asignar.append(colores[row])
plt.scatter(x, y, c=asignar, s=1)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='black', s=20) # Marco centroides.
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Pokemon Attack Defense k-means clustering')
plt.show()

#Dendograma de correlaciones
import seaborn as sns
correlaciones = pokemon.corr()
sns.clustermap(correlaciones,method="complete",cmap="RdBu",annot=True,annot_kws={"size":15},vmin=-1, vmax=1,figsize=(15,12))

#Representación de los clusters en Excel
centroides = pokemon.groupby(by=("cluster"),as_index=False).mean()
centroides.to_excel("pokemoncluster2.xlsx")
pokemon.cluster.value_counts()




# =============================================================================
# ##~  Primer Ejercicio. Samsunng
# =============================================================================


import pandas as pd
from sklearn import preprocessing 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Carga del dataframe.
samsung = pd.read_csv("C:/Users/Javi/Desktop/INMUNE/CURSO IMMUNE 3AÑO/Datos/Samsung.csv")
datoskmeans = samsung.loc[:,["Close","Volume"]]


datoskmeans = datoskmeans.dropna()
datoskmeans= datoskmeans.reset_index(drop=True)




#%% Se normalizan los datos con MinMax()
min_max_scaler = preprocessing.MinMaxScaler() 
datos_escalados = min_max_scaler.fit_transform(datoskmeans)
datos_escalados = pd.DataFrame(datos_escalados) # Hay que convertir a DF el resultado.
datos_escalados = datos_escalados.rename(columns = {0: 'Close', 1: 'Volume'})



x = datos_escalados['Close'].values
y = datos_escalados['Volume'].values
plt.xlabel('Close price')
plt.ylabel('Volume')
plt.title('Samsung stocks CLOSE vs. VOLUME')
plt.plot(x,y,'o',markersize=1)

from plotnine import * 
elbow_values = []
for i in range(1,11,1):
    km = KMeans(n_clusters=i)
    km.fit(datos_escalados)
    elbow_values.append(km.inertia_)
elbow = pd.DataFrame({"clusters":range(1,11,1), "elbow" : elbow_values})    
    
ggplot(aes(x = "clusters", y ="elbow"),elbow)+geom_line()+geom_point()+ggtitle("Elbow graph")

#%% Aplicación de k-means con k = 5.
kmeans = KMeans(n_clusters=4).fit(datos_escalados)
centroids = kmeans.cluster_centers_
print(centroids)


#%% Etiquetamos nuestro dataframe.
cluster = kmeans.predict(datos_escalados)
samsung['cluster'] = cluster

colores=['red','green','blue','yellow']
asignar=[]
for row in cluster:
     asignar.append(colores[row])
plt.scatter(x, y, c=asignar, s=1)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='black', s=20) # Marco centroides.
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Pokemon Attack Defense k-means clustering')
plt.show()

import seaborn as sns
correlaciones = samsung.corr()
#pokemon = pokemon.drop("cluster",axis=1)
sns.clustermap(correlaciones,method="complete",cmap="RdBu",annot=True,annot_kws={"size":15},vmin=-1,vmax=1,figsize=(15,12))


centroides = samsung.groupby(by=("cluster"),as_index=False).mean()
centroides.to_excel("Samusng2.xlsx")
samsung.cluster.value_counts()

