import pandas as pd
import datetime as dt

def main():
    eje_1()
    eje_2()
    eje_3()
    eje_4()
    eje_5()
    eje_6()
    eje_7()
    create_custom_dataset()

def eje_1():
    dataset_2019 = data[data['Fecha'].dt.year == 2019]
    print(f'Data set 2019: \n{dataset_2019}')

def eje_2():
    orders_per_day = data['Fecha'].dt.date.value_counts().sort_index()
    print(f'Orders per day: \n{orders_per_day}')

def eje_3():
    products_sold_per_day = data.groupby(data['Fecha'].dt.date)['Cantidad'].sum()
    print(products_sold_per_day)

def eje_4():
    data['Coste_Total'] = data['Cantidad'] * data['Precio Coste']
    print(f'Cost price per quantity: {data.Coste_Total}')

def eje_5():
    print(f'Base price: \n {data.Base}')

def eje_6():
    print(f'Total price: \n {data.Total}')

def eje_7():
    data['Mes'] = data['Fecha'].dt.month
    data['Dia_semana'] = data['Fecha'].dt.weekday + 1 
    data['Día'] = data['Fecha'].dt.day
    print(data[['Mes', 'Dia_semana', 'Día']])

def create_custom_dataset():
    data_2019 = data[data['Fecha'].dt.year == 2019]
    data_2019 = data_2019[['Fecha', 'Familia', 'Precio', 'Precio Coste', 'Cantidad']]
    data_2019['Precio Total'] = data_2019['Cantidad'] * data_2019['Precio']
    new_2019_dataset = data_2019.groupby(data_2019['Fecha']).agg(
    Familia=('Familia', 'first'),
    Precio_articulo=('Precio','first'),
    Precio_coste=('Precio Coste', 'sum'),
    Pedidos_por_día=('Fecha', 'size'),
    Precio_total_por_día=('Precio Total', 'sum'),
    ).reset_index()
    print(new_2019_dataset)

def load_datasets():
    alcala = pd.read_excel("Datasets\ProyectoPandas\\alcala.xlsx")
    barcelona = pd.read_excel("Datasets\ProyectoPandas\\barcelona.xlsx")
    las_tablas = pd.read_excel("Datasets\ProyectoPandas\las_tablas.xlsx")
    malasana = pd.read_excel("Datasets\ProyectoPandas\malasaña.xlsx")
    mallorca = pd.read_excel("Datasets\ProyectoPandas\mallorca.xlsx")
    paracuellos = pd.read_excel("Datasets\ProyectoPandas\paracuellos.xlsx")
    pozuelo = pd.read_excel("Datasets\ProyectoPandas\\pozuelo.xlsx")
    valencia = pd.read_excel("Datasets\ProyectoPandas\\valencia.xlsx")
    dataframes = [alcala, barcelona, las_tablas, malasana, mallorca, paracuellos, pozuelo, valencia]
    return dataframes

def create_master_dataset():
    dataset_master = pd.concat(dataframes, ignore_index=True)
    dataset_master.to_excel("Ejercicios\Proyectos\dataset_master.xlsx", index=False)

if __name__ == "__main__":
    # dataframes = load_datasets()
    # create_master_dataset()
    data = pd.read_excel("Ejercicios\Proyectos\dataset_master.xlsx")
    data['Fecha'] = pd.to_datetime(data['Fecha']) # Aseguramos que la variable Fecha se datetime
    main()
