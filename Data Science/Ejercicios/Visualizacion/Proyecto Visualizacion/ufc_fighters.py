# -*- coding: utf-8 -*-
# https://www.data-to-viz.com/#connectedscatter

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


# Cargando el conjunto de datos
ufc_data = pd.read_csv('C:/Users/Adri/Documents/Tercer-Curso/Data Science/Ejercicios/Visualizacion/Proyecto Visualizacion/ufc-fighters-statistics.csv')

def revision_dataset():
    # Revisando la informacion general y buscando valores faltantes
    info_general = ufc_data.info()
    valores_faltantes = ufc_data.isnull().sum()
    info_general, valores_faltantes

def limpieza_dataset():
    # Convertir 'date_of_birth' a tipo fecha
    ufc_data['date_of_birth'] = pd.to_datetime(ufc_data['date_of_birth'], errors='coerce')

    # Creando una nueva columna para la edad de los luchadores (basada en la fecha actual)
    current_year = pd.Timestamp.now().year
    ufc_data['age'] = current_year - ufc_data['date_of_birth'].dt.year

    # Reemplazando valores faltantes en 'height_cm', 'weight_in_kg', y 'reach_in_cm' con la media
    ufc_data['height_cm'].fillna(ufc_data['height_cm'].mean(), inplace=True)
    ufc_data['weight_in_kg'].fillna(ufc_data['weight_in_kg'].mean(), inplace=True)
    ufc_data['reach_in_cm'].fillna(ufc_data['reach_in_cm'].mean(), inplace=True)

# Distribucion entre Victorias, Derrotas y empates.
def primera_figura():
    # Configurando el estilo de los gráficos
    plt.style.use('seaborn-whitegrid')
    
    # Creando un gráfico de barras para visualizar la distribución de victorias, derrotas y empates
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Victorias
    ufc_data['wins'].plot(kind='hist', bins=20, color='green',range=(0,50),edgecolor='black', ax=axes[0])
    axes[0].set_title('Distribución de Victorias')
    axes[0].set_xlabel('Victorias')
    axes[0].set_ylabel('Frecuencia')
    
    # Derrotas
    ufc_data['losses'].plot(kind='hist', bins=20, color='red',range=(0,35),edgecolor='black', ax=axes[1])
    axes[1].set_title('Distribución de Derrotas')
    axes[1].set_xlabel('Derrotas')
    
    # Empates
    ufc_data['draws'].plot(kind='hist', bins=20, color='blue', range=(0,6), edgecolor='black',ax=axes[2])
    axes[2].set_title('Distribución de Empates')
    axes[2].set_xlabel('Empates')
    
    plt.tight_layout()
    plt.show()

# Relación entre Altura, Peso, Alcance y Victorias
def segunda_figura():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Relación entre la altura y las victorias
    axes[0].scatter(ufc_data['height_cm'], ufc_data['wins'], color="green",marker='x')
    axes[0].set_title('Altura vs. Victorias')
    axes[0].set_xlabel('Altura (cm)')
    axes[0].set_ylabel('Victorias')
    axes[0].set_ylim([0, 100])
    
    # Relación entre el peso y las victorias
    axes[1].scatter(ufc_data['weight_in_kg'], ufc_data['wins'], color="blue",marker='x')
    axes[1].set_title('Peso vs. Victorias')
    axes[1].set_xlabel('Peso (kg)')
    axes[1].set_xlim([45, 200]) 
    axes[1].set_ylim([0, 100]) 
    
    # Relación entre el alcance y las victorias
    axes[2].scatter(ufc_data['reach_in_cm'], ufc_data['wins'], color="red",marker='x')
    axes[2].set_title('Alcance vs. Victorias')
    axes[2].set_xlabel('Alcance (cm)')
    axes[2].set_ylim([0, 100])
    
    plt.tight_layout()
    plt.show()
    
# Estudio del rendimiento en base a la edad
def tercera_figura():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Relación entre la edad y las victorias
    axes[0].scatter(ufc_data['age'], ufc_data['wins'], color="green", marker='x')
    axes[0].set_title('Edad vs. Victorias')
    axes[0].set_xlabel('Edad')
    axes[0].set_ylabel('Victorias')
    axes[0].set_ylim([0, 50])
    
    # Relación entre la edad y las derrotas
    axes[1].scatter(ufc_data['age'], ufc_data['losses'], color="red", marker='x')
    axes[1].set_title('Edad vs. Derrotas')
    axes[1].set_xlabel('Edad')
    axes[1].set_ylabel('Derrotas')
    axes[1].set_ylim([0, 50])
    
    # Relación entre la edad y los empates
    axes[2].scatter(ufc_data['age'], ufc_data['draws'], color="blue", marker='x')
    axes[2].set_title('Edad vs. Empates')
    axes[2].set_xlabel('Edad')
    axes[2].set_ylabel('Empates')
    axes[2].set_ylim([0, 12])
    
    plt.tight_layout()

# Estudio de los distintos estilos de lucha distribuidos por categorias.
def cuarta_figura():
    # Definimos los límites de las categorías de peso de la UFC y las etiquetas.
    bins = [0, 52.5, 56.7, 65.8, 70.3, 77.1, 83.9, 102.1, 120.2, float('inf')]
    labels = ['Strawweight', 'Flyweight','Featherweight','Lightweight', 'Welterweight', 'Middleweight', 'Light Heavyweight',
              'Heavyweight', 'Super Heavyweight']
    
    # Utilizamos pd.cut para crear la nueva columna 'weight_class'
    ufc_data['weight_class'] = pd.cut(ufc_data['weight_in_kg'], bins=bins, labels=labels, include_lowest=True)
    
    # Eliminamos cualquier fila donde 'stance' sea NaN para evitar problemas en el agrupamiento
    ufc_data_clean = ufc_data.dropna(subset=['stance'])
    
    # Agrupamos en torno a 'weight_class' y 'stance'
    grouped_data = ufc_data_clean.groupby(['weight_class', 'stance']).size().unstack(fill_value=0)
    
    # Normalizamos los datos para que se muestren mejor los datos en el mapa de calor
    heatmap_data = grouped_data.div(grouped_data.sum(axis=1), axis=0)
    
    # Creamos el mapa de calor
    fig, ax = plt.subplots(figsize=(12, 8))
    cax = ax.matshow(heatmap_data, cmap='coolwarm')
    
    plt.colorbar(cax)
    
    ax.set_xticks(np.arange(len(heatmap_data.columns)))
    ax.set_xticklabels(heatmap_data.columns, rotation=90)
    ax.set_yticks(np.arange(len(heatmap_data.index)))
    ax.set_yticklabels(heatmap_data.index)
    
    # Añadimos los nombres a la variables y el titulo
    plt.title('Heatmap of Stance Distribution by Weight Class')
    plt.xlabel('Stance')
    plt.ylabel('Weight Class')
    
    # Mostramos el mapa
    plt.show()
        
# Comparación de la eficacia de diferentes estilos de lucha
def quinta_figura():
    fight_styles_data = ufc_data[['stance', 'significant_strikes_landed_per_minute', 'significant_striking_accuracy']]

    # Creando un gráfico de caja para visualizar la eficacia de diferentes estilos de lucha
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    
    # Golpes significativos aterrizados por minuto por estilo de lucha
    fight_styles_data.boxplot(column='significant_strikes_landed_per_minute', by='stance', ax=axes[0])
    axes[0].set_title('Estilo de Lucha vs. Golpes Significativos Aterrizados por Minuto')
    axes[0].set_xlabel('Estilo de Lucha')
    axes[0].set_ylabel('Golpes Significativos por Minuto')
    
    # Precisión de golpes significativos por estilo de lucha
    fight_styles_data.boxplot(column='significant_striking_accuracy', by='stance', ax=axes[1])
    axes[1].set_title('Estilo de Lucha vs. Precisión de Golpes Significativos')
    axes[1].set_xlabel('Estilo de Lucha')
    axes[1].set_ylabel('Precisión de Golpes Significativos (%)')
    
    # Ajustar las gráficas para evitar la superposición de títulos
    plt.suptitle('')
    plt.tight_layout()
    
    # Mostrando los gráficos
    plt.show()
   
# Comparación de la eficacia de diferentes estilos de pelea en función de la defensa
def sexta_septima_figura():
    # Primero, preparamos los datos para los gráficos de violín agrupando por 'stance'.
    grouped_strikes = ufc_data.groupby('stance')['significant_strikes_absorbed_per_minute']
    grouped_defence = ufc_data.groupby('stance')['significant_strike_defence']
    
    # Inicializamos la figura y los ejes para el primer gráfico de violín
    fig, ax1 = plt.subplots(figsize=(8, 6))
    
    # Creamos el gráfico de violín para 'significant_strikes_absorbed_per_minute'
    violins1 = ax1.violinplot([group[1].values for group in grouped_strikes],
                              showmeans=False, showmedians=True)
    
    # Definimos colores para cada grupo
    colors = ['orange', 'purple', '#69b3a2', 'blue', 'green']
    
    # Asignamos colores a cada violín en el gráfico de violín
    for violin, color in zip(violins1['bodies'], colors[:len(violins1['bodies'])]):
        violin.set_facecolor(color)
    
    # Añadimos título y etiquetas de los ejes
    ax1.set_title('Golpes Significativos Absorbidos por Minuto por Estilo de Pelea', weight='bold')
    ax1.set_ylabel('Golpes Significativos Absorbidos por Minuto')
    ax1.set_xticks(np.arange(1, len(grouped_strikes.groups.keys()) + 1))
    ax1.set_ylim(0, 30)
    ax1.set_xticklabels(grouped_strikes.groups.keys())
    
    # Inicializamos la figura y los ejes para el segundo gráfico de violín
    fig, ax2 = plt.subplots(figsize=(8, 6))
    
    # Creamos el gráfico de violín para 'significant_strike_defence'
    violins2 = ax2.violinplot([group[1].values for group in grouped_defence],
                              showmeans=False, showmedians=True)
    
    # Asignamos colores a cada violín en el gráfico de violín
    for violin, color in zip(violins2['bodies'], colors[:len(violins2['bodies'])]):
        violin.set_facecolor(color)
    
    # Añadimos título y etiquetas de los ejes
    ax2.set_title('Defensa de Golpes Significativos por Estilo de Pelea', weight='bold')
    ax2.set_ylabel('Defensa de Golpes Significativos (%)')
    ax2.set_xticks(np.arange(1, len(grouped_defence.groups.keys()) + 1))
    ax2.set_xticklabels(grouped_defence.groups.keys())
    
    # Mostramos los gráficos
    plt.show()
    
# Relación entre precisión y defensa de takedowns en base a las victorias y categoría de peso.
def octava_figura():
    bins = [0, 52.5, 56.7, 65.8, 70.3, 77.1, 83.9, 102.1, 120.2, float('inf')]
    labels = ['Strawweight', 'Flyweight', 'Featherweight', 'Lightweight', 
              'Welterweight', 'Middleweight', 'Light Heavyweight', 
              'Heavyweight', 'Super Heavyweight']
    ufc_data['weight_class'] = pd.cut(ufc_data['weight_in_kg'], bins=bins, labels=labels, include_lowest=True)
    
    # Creando el gráfico de burbujas con Plotly
    bubble_chart = px.scatter(ufc_data, 
                              x='takedown_accuracy', 
                              y='takedown_defense', 
                              color='weight_class',
                              size='wins', 
                              hover_name='name', 
                              title='Relación entre Precisión y Defensa de Takedowns por Categoría de Peso',
                              labels={'takedown_accuracy': 'Precisión de Takedowns', 
                                      'takedown_defense': 'Defensa de Takedowns'})
    
    # Mostrando el gráfico
    bubble_chart.show(renderer='browser')

# Relación entre porcentaje de takedowns y porcentaje de sumisiones cada 15 minutos en base a las victorias y categoría de peso.
def novena_figura():
    bins = [0, 52.5, 56.7, 65.8, 70.3, 77.1, 83.9, 102.1, 120.2, float('inf')]
    labels = ['Strawweight', 'Flyweight', 'Featherweight', 'Lightweight', 
              'Welterweight', 'Middleweight', 'Light Heavyweight', 
              'Heavyweight', 'Super Heavyweight']
    ufc_data['weight_class'] = pd.cut(ufc_data['weight_in_kg'], bins=bins, labels=labels, include_lowest=True)
    
    # Creando el gráfico de burbujas con Plotly
    bubble_chart = px.scatter(ufc_data, 
                              x='average_takedowns_landed_per_15_minutes', 
                              y='average_submissions_attempted_per_15_minutes', 
                              color='weight_class',
                              size='wins', 
                              hover_name='name', 
                              title='Relación entre Derribos y Intentos de Sumisión por Categoría de Peso',
                              labels={'average_takedowns_landed_per_15_minutes': 'Promedio de Derribos cada 15 Minutos', 
                                      'average_submissions_attempted_per_15_minutes': 'Promedio de Intentos de Sumisión cada 15 Minutos'},
                              range_x=[0, 15]) # Limitando el eje x a 15)

        
    # Mostrando el gráfico
    bubble_chart.show(renderer='browser')
    
# Relación entre el porcentaje de golpeo y defensas en base a las victorias y categoría de peso.
def decima_figura():
    bins = [0, 52.5, 56.7, 65.8, 70.3, 77.1, 83.9, 102.1, 120.2, float('inf')]
    labels = ['Strawweight', 'Flyweight', 'Featherweight', 'Lightweight', 
              'Welterweight', 'Middleweight', 'Light Heavyweight', 
              'Heavyweight', 'Super Heavyweight']
    ufc_data['weight_class'] = pd.cut(ufc_data['weight_in_kg'], bins=bins, labels=labels, include_lowest=True)
    
    # Creando el gráfico de burbujas con Plotly
    bubble_chart = px.scatter(ufc_data, 
                              x='significant_striking_accuracy', 
                              y='significant_strike_defence', 
                              color='weight_class',
                              size='wins', 
                              hover_name='name', 
                              title='Relación entre Golpes significativos y Defensa significativa',
                              labels={'significant_striking_accuracy': 'Porcentaje de golpes significativos', 
                                      'significant_strike_defence': 'Defensa de golpe significativos'})

    # Mostrando el gráfico
    bubble_chart.show(renderer='browser')
