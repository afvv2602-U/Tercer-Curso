# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:51:43 2023

@author: Adri
"""
from plotnine import *
#from plotnine.data import *
import pandas as pd

def main():
    data = pd.read_excel("C:/Users/Adri/Documents/Tercer-Curso/Data Science/Datasets/netflix.xlsx")
#1 crea un grafico de barras  de películas y programas de televisión
def eje_1():
    mv_tv = data['type'].value_counts().reset_index()
    mv_tv.columns = ['type', 'count']
    ggplot(aes(x='type',y='count'),mv_tv)+geom_bar(position='dodge',stat='identity')
    
#2 crea un grafico de barras de los 10 mejores directores por recuento de películas
def eje_2():
    top_directors = (data[data['type'] == 'Movie'].groupby('director')['title'].count().reset_index(name='count')
                 .sort_values(by='count', ascending=False).head(10))
    ggplot(aes(x='director',y='count'),top_directors)+geom_bar(stat='identity')\
        +xlab('Director')+ylab('Count')+ggtitle('Top 10 directores por peliculas')\
            +theme(axis_text_x=element_text(rotation=90, hjust=1))
    
#3 Gráfico de dispersión(scatterplot) de la duración de la película VS a los releas_year
def eje_3():
    

#4 Gráfico de dispersión de calificaciones de VS frente a Release Years


#5 Histograma de duración de programas de televisión


#6 Gráfico de barras de los 10 principales países por recuento de títulos de pelis


#7 Gráfico de barras de los 10 géneros principales por número de títulos pelis


#8 Gráfico de barras de distribución de ratings


#9 Gráfico de barras agrupadas de recuentos de películas y programas de televisión por año


#10 Gráfico de barras agrupadas de género cuenta por tipo


#11 grafico de barras  de películas y programas de televisión por país


#12 Gráfico de barras horizontales de los 10 mejores directores por recuento de películas


#13 Histograma  de duración de programas de televisión por clasificación