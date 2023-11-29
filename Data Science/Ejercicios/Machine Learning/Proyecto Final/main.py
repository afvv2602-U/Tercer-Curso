# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:26:29 2023

@author: Adri
"""

#%%  Imports
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


#%% Data Clean and KMean

data = pd.read_excel("C:/Users/Adri/Documents/Tercer-Curso/Data Science/Ejercicios/Machine Learning/Proyecto Final/HR Data.xlsx")

datos_kmeans = data.loc[:,['CF_age band','Monthly Income','Education']]

# Convertir datos categóricos en numéricos
age = LabelEncoder()
education = LabelEncoder()
datos_kmeans['CF_age band'] = age.fit_transform(datos_kmeans['CF_age band'])
datos_kmeans['Education'] = education.fit_transform(datos_kmeans['Education'])

# Normalización de los datos
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(datos_kmeans)

# Mostramos los primeros registros del conjunto de datos normalizado
pd.DataFrame(normalized_data, columns=datos_kmeans.columns).head()


#%% Metodo del codo

distortions = []
K = range(1, 10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(normalized_data)
    distortions.append(kmeanModel.inertia_)

# Graficando el método del codo
plt.figure(figsize=(12, 6))
plt.plot(K, distortions, 'bx-')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Distorsión')
plt.title('Método del Codo para determinar el número óptimo de clusters')
plt.show()


#%% Silueta
from sklearn.metrics import silhouette_score

silhouette_scores = []
K = range(2, 10)  # Empezamos desde 2 porque no se puede calcular la silueta para k=1
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    cluster_labels = kmeanModel.fit_predict(normalized_data)
    silhouette_scores.append(silhouette_score(normalized_data, cluster_labels))

# Graficando el análisis de silueta
plt.figure(figsize=(12, 6))
plt.plot(K, silhouette_scores, 'bo-')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Puntaje de Silueta')
plt.title('Análisis de Silueta para determinar el número óptimo de clusters')
plt.show()


#%% Creacion de los clusters 3D
from mpl_toolkits.mplot3d import Axes3D

kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(normalized_data)

# Creando el scatter plot 3D de los clusters
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(normalized_data[:, 0], normalized_data[:, 1], normalized_data[:, 2], c=labels, cmap='viridis', marker='o')
centers = kmeans.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='crimson', s=400, alpha=1, marker='x')  # Centros más grandes
ax.set_title('Visualización 3D de los clusters para k=4', fontsize=20)
ax.set_xlabel('Banda de Edad Normalizada', fontsize=14, labelpad=15)
ax.set_ylabel('Ingreso Mensual Normalizado', fontsize=14, labelpad=15)
ax.set_zlabel('Educación Normalizada', fontsize=14, labelpad=15)
plt.savefig('cluster_visualization.png', dpi=300) 
plt.show()

#%% Creacion de los clusters en 2D

def plot_clusters(data, labels, centers, column_indices, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[:, column_indices[0]], data[:, column_indices[1]], c=labels, cmap='viridis', marker='o')
    plt.scatter(centers[:, column_indices[0]], centers[:, column_indices[1]], c='red', s=200, alpha=0.75, marker='x')
    plt.title(title)
    plt.xlabel(datos_kmeans.columns[column_indices[0]])
    plt.ylabel(datos_kmeans.columns[column_indices[1]])
    plt.show()
    
plot_clusters(normalized_data, labels, centers, [0, 1], 'Edad vs Ingreso Mensual')
plot_clusters(normalized_data, labels, centers, [0, 2], 'Edad vs Educación')
plot_clusters(normalized_data, labels, centers, [1, 2], 'Ingreso Mensual vs Educación')


#%%

