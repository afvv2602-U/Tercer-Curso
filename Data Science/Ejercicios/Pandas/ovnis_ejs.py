import pandas as pd
import datetime as dt

def main():
    print(data.columns)
    # eje_67()
    # eje_68()
    # eje_69()
    # eje_70()
    # eje_71()
    eje_72()
    eje_73()
    eje_74()
    eje_75()
    eje_76()

def eje_67():
    x = dt.date.today()
    print(x)

def eje_68():
    data['date_time_clean'] = pd.to_datetime(data['date_time'])
    print(data['date_time_clean'])

def eje_69():
    data['date_time_clean'] = pd.to_datetime(data['date_time'])
    time_difference =(dt.datetime.now() - data['date_time_clean'].min())
    print(time_difference)

def eje_70():
    # Mi forma
    data['date_time_clean'] = pd.to_datetime(data['date_time'])
    fourty_years = dt.datetime.now() - dt.timedelta(days=365*40)
    reports = data[(data['date_time_clean'] >= fourty_years)]
    print(reports)  

    # Forma del profe
    data['date_time_clean'] = pd.to_datetime(data['date_time'])
    data['año'] = data['date_time_clean'].dt.year
    data['mes'] = data['date_time_clean'].dt.month
    data['dia'] = data['date_time_clean'].dt.day
    select_period = data[(data['año'] >= 1983)]
    print(select_period)

def eje_71():
    data['date_time_clean'] = pd.to_datetime(data['date_time'])
    select_period = data[data['date_time_clean'].between('1970-10-10','1980-10-10')]
    print(select_period)

def eje_72():
    pass

def eje_73():
    pass

def eje_74():
    pass

def eje_75():
    pass

def eje_76():
    pass

if __name__ == "__main__":
    data = pd.read_csv("Datasets\\nuforc_reports_clean.csv")

    main()