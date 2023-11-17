from plotnine import *
from plotnine.data import *
import pandas as pd

"""
Sintaxis

ggplot(aes(x='',y='',),dataset)+type_of_visualacer(geom_bar(),line(),point()....)

"""
# Scatterplots
def scatterplots(): 
    # Creamos un scatterplot con 2 variables
    ggplot (aes("displ","hwy"),mpg)+geom_point()

    # Crear una tercera dimension
    ggplot (aes("displ","hwy",color='class'),mpg)+geom_point()

    # Agregar diferentes formas a los puntos
    ggplot (aes("displ","hwy",color='class'),mpg)\
        +geom_point(aes(shape='factor(cyl)'))
    
    # Agregar titulos a los ejes y al grafico
    ggplot (aes("displ","hwy",color='class'),mpg)\
        +geom_point(aes(shape='factory(cyl)'))\
        +xlab("Eje x")+ylab('Eje y')+ggtitle("HWY vs DIPL")
    
    # Mapeos esteticos, modifico la escala de colores
    ggplot (aes("displ","hwy",color='class'),mpg)+geom_point(aes(color='cyl'))\
        +scale_color_gradient(low='red',high='blue')

    # Modificar el tamaño de los puntos
    ggplot (aes("displ","hwy",color='class'),mpg)+geom_point(aes(size='hwy'))
    ggplot (aes("displ","hwy",color='class'),mpg)+geom_point(aes(size='3',color='blue'))

    # Agregar un theme
    ggplot (aes("displ","hwy",color='class'),mpg)+geom_point(aes(shape='factory(cyl)'))\
        +xlab("Eje x")+ylab("Eje y")+ggtitle("HWY vs DISPL")+theme_classic()
    
def bar_data_set():

    # Correlacion positiva
    ggplot(aes("items","bill"),bar)+geom_point() # Ver correlacion entre variables
    ggplot(aes("items","bill",color='gender'),bar)+geom_point() # Ver correlacion entre variables pero usando genero para el color

    ggplot(aes("items","bill",color='service'),bar)+geom_point()\
        +xlim(50,200)
    
    # No hay correlacion
    ggplot(aes("items","tip",color='gender'),bar)+geom_point() # No hay correlaciones

def histograms():
    # Creacion de un histograma simple
    ggplot(aes("bill"),bar)+geom_histogram()

    # Añadimos variable fill
    ggplot(aes("bill",fill='service'),bar)+geom_histogram() # Fill rellena y color hace el borde

    # Facet_grid que te divide el grafico en las variables en este caso crea 5 graficos
    ggplot(aes("bill",fill='service'),bar)+geom_histogram()\
        +facet_grid(('service','.')) 

    # Aqui se divide por tipo de servicio y genero
    ggplot(aes("bill",fill='service'),bar)+geom_histogram()\
        +facet_grid(('service','gender'))

def barplots():
    # Crear un bar plot con la variable service
    ggplot(aes('service'),bar)+geom_bar()
    bar.service.value_counts()
    
    # Movemos el grafico 90 grados
    ggplot(aes('service'),bar)+geom_bar()+coord_flip()
    
    # Coloreamos el grafico colorbrewer.com
    ggplot(aes('service'),bar)+geom_bar()\
            +scale_fill_brewer(type='seq',palette='BuPu')
    
    ggplot(aes('service'),bar)+geom_bar()\
            +scale_fill_brewer(type='seq',palette='Pastel2')
            
    ggplot(aes('service'),bar)+geom_bar()\
            +scale_fill_brewer(type='seq',palette='RdGy')
            
    # Graficos de barras agrupados (3 Tipos)
    
    # Barras juntas en vez de agrupadas
    ggplot(aes('gender',fill='service'),bar)+geom_bar(position='dodge') # Para separar cada resultado
    
    # Frecuencias absolutas
    ggplot(aes('gender',fill='service'),bar)+geom_bar(position='stack') # Igual que el grafico sin modificar

    # Frecuencias relativas
    ggplot(aes('gender',fill='service'),bar)+geom_bar(position='fill') # Por porcentajes
    
    # geom_col()
    ggplot(aes('service',y='bill'),bar)+geom_col() # Suma los resultados de bill a la columna service aqui siempre necesitas x e y
    
    ggplot(aes('service',y='bill'),bar)+geom_bar(stat='identity') # Lo mismo pero con geom_bar() pero puedes solo usar una variable
    
    # Stat = identity
    
    bar2 = bar.loc[:,['service','bill','gender']].groupby(by=['service','gender'],as_index=False).sum()
    
    # Barras juntas en vez de agrupadas
    ggplot(aes('gender',y='bill',fill='service'),bar)+geom_bar(position='dodge',stat='identity')
    ggplot(aes('gender',y='bill',fill='service'),bar)+geom_bar(position='dodge')

    
    # Frecuencias absolutas
    ggplot(aes('gender',y='bill',fill='service'),bar)+geom_bar(position='stack',stat='identity')

    # Frecuencia relativa
    ggplot(aes('gender',y='bill',fill='service'),bar)+geom_bar(position='fill',stat='identity')

    # density
    ggplot(aes('bill',fill='service'),bar)+geom_density()+facet_wrap('service') # Se ejecuta con una sola en vertical
    
    ggplot(aes('bill',fill='service'),bar)+geom_density()+facet_grid(('service','.')) # Necesita dos variables
    
    ggplot(aes('bill',fill='service'),bar)+geom_density()+facet_grid(('service','nationality'))\
        +slace_fill_brewer(type='div',palette='RdGy')
        
        
def heat_maps():
    # Crear un heat map con 3 variables
    ggplot(aes('factor(week_day)','month',fill='bill'),bar)+geom_tile(color='white',size=1)\
        +scale_fill_gradient(low='lightblue',high='blue')
        
    data2 = bar.groupby(by=['month','nationality'],as_index=False).sum()
    data2.tip = data2.tip.round()
    ggplot(aes('factor(month)','nationality',fill='tip'),data2)+geom_tile(color='white',size=1)\
        +scale_fill_gradient(low='lightblue',high='blue')+theme_classic()\
            +geom_text(label='tip',size=8,color='black')
            
        
    
    

if __name__ == "__main__":
    bar = pd.read_excel("Documents/Tercer-Curso/Data Science/Datasets/bar.xlsx")


