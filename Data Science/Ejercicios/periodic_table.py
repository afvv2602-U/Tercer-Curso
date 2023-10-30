import pandas as pd

def main():
    pass

def read():
    # Mostrar los nombres de las columnas
    cols = data.columns 
    # Nos da todo los datos del data set
    des = data.describe()

    dimesiones = data.shape # Dimensiones del dataset

    # Ver las 5 primera filas.
    x = data.head(5)

    # Podemos especificar cuantas filas queremos ver desde el final en esta caso 10
    z = data.tail(10)

    # Ver el tipo de dato
    types = data.dtypes

    # Crear una columna nueva al final
    data["logica"] = False

    # Filtrado y manipulacion de datos

    #.iloc para extraer por el indice numerico
    #.loc para extraer por nombre
                 #Fila    Columna
    c = data.loc[     :,["AtomicNumber","Element"] ] # Estamos sacando todas las filas de las columnas AtomicNumber y Element, creando una lista nueva
    c = data.iloc[0,:] # Cogemos todas las columnas de la fila 1
    c = data.iloc[:,5:8] # Cogemos desde la posicion 5 a la 7 con todas las filas
    c = data.iloc[2:6,:] # Cogemos de las filas 2 a 5 con todas las columnas
    # Sacamos el valor 1 y 2 de las filas y despues con loc filtramos las columnas necesarias de las columnas AtomicNumber y Element
    c = data.iloc[1:3,:].loc[:,["AtomicNumber","Element"]] 
    
    # Filtrar por condicionales
    x = data.loc[data.AtomicMass>280,:] # Sacamos todas las columnas de las filas que sean mayores de 280

    x = data.loc[(data.AtomicMass>280)&(data.Metal == 'yes'),:] # Unimos dos condicionales con el simbolo &

    # Renombrar columnas
    data.rename(columns={"AtomicNumber":"NumeroAtomico"},inplace=True) # inplace=True modifica el data si fuese false solo mostraria la operacion

# Duplicados
def duplicates():
    data.drop("Element",axis=1,inplace=True) # Borrar la columna Element axis=1 especificas que sean columnas axis=0 las filas

    c = data.dropna(axis=1) # Borramos las columnas NA (Not available)

    v = data.dropna(subset=["Type"],inplace=True) # Borramos las filas cuyos valores de Type sean nulos

    x = data.drop_duplicates(subset=["Discoverer"],keep="first") # Borramos las filas cuyo Dicoverer este duplicado y nos quedamos con el primero que aparezca 
    
# Valores NAN
def na_values():
    data.isnull().values.any() # Con este comando vemos si hay valores nulos en este Dataset

    x = data.isnull() # Devuelve el dataset entero en True o False, dependiendo True es que el valor es Null False tiene valor

    # Contar los valores nulos de un dataset por variables

    data.isnull().sum() # Te devuelve cuantos valores nulos hay por cada columna

    data.isnull().sum().sum() # Suma total de todos los valores nulos

    data.Metal.isnull() # Seleccionamos las filas de los valores nulos de la columna Metal

    data.columns[data.isnull.any()] # Nos devuelve todas las variables que tienen valores nulos
  
# Rellenar valores nulos
def fill_na():
    data.fillna(value=44444,inplace=True) # Rellenamos todos los valores NA con 444444 sean numericos o no

    data.Year.fillna(value=2023,inplace=True) # Rellenamos todos los valores NA de la variable Year con el valor 2023

    data.fillna(value=data.mean(),inplace=True) # Rellenamos todos los valores NA de todas las variables numericas usando la media de cada variable

    data["MeltingPoint"].fillna(value=data["MeltingPoint"].mean(),inplace=True) # Rellenamos todos los NA de la variables MeltingPoint con la media de la col
    data.MeltingPoint.fillna(value=data.MeltingPoint.mean(),inplace=True) # Otra forma de hacer lo mismo

    data.Metal.fillna("no info",inplace=True) # Actualizamos los NA de metal a no info


if __name__ == "__main__":
    data = pd.read_csv("Datasets\Periodic Table of Elements.csv")
    main()