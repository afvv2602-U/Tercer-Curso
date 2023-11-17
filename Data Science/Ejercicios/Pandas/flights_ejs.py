import pandas as pd

def main():
    print(flights.columns)
    print(normal.columns)
    print(premiun.columns)
    print(categories.columns)
    print(tickets.columns)
    # eje_47()
    # eje_48()
    # eje_49()
    # eje_50()
    # eje_51()
    # eje_52()
    eje_53()
    eje_54()
    eje_55()

def eje_47():
    age_mean = premiun['Age'].mean()
    age_mean_men = premiun.loc[premiun.Gender == 'M']['Age'].mean()
    print(f'Mean age {age_mean}, Mean age of men {age_mean_men}')

def eje_48():
    passengers = pd.concat([normal,premiun])
    print(passengers)

def eje_49():
    values = flights.Time.value_counts()
    print(f'{values}')

def eje_50():
    flights['duracion_vuelos'] = pd.cut(flights.Duration,bins=[0,5,10,flights.Duration.max()],labels=['Corto','Mediano','Largos'])
    print(flights.duracion_vuelos)

def eje_51():
    passengers = pd.concat([normal,premiun])
    x = passengers.Gender.value_counts()
    print(x)

def eje_52():
    x = tickets[tickets['Passenger'].str.startswith('P')].count()
    y = tickets[tickets['Passenger'].str.startswith('N')].count()
    print(f'Premium {x}, Normal {y}')

    x = pd.merge(tickets,premiun,left_on='Passenger',right_on='ID',how='left')
    y = pd.merge(tickets,normal,left_on='Passenger',right_on='ID',how='left')
    print(f'Premium {x.Category.value_counts()}, Normal {y.Category.value_counts()}')

def eje_53():
    x = pd.merge(flights,tickets,left_on='Time',right_on='TicketID',how='left')
    print(x)

def eje_54():
    pass

def eje_55():
    pass

if __name__ == "__main__":
    flights = pd.read_excel("Datasets\\flights.xlsx")
    normal = pd.read_excel("Datasets\\flights.xlsx",sheet_name=1)
    premiun = pd.read_excel("Datasets\\flights.xlsx",sheet_name=2)
    categories = pd.read_excel("Datasets\\flights.xlsx",sheet_name=3)
    tickets = pd.read_excel("Datasets\\flights.xlsx",sheet_name=4)
    main()