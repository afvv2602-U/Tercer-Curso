from plotnine import *
from plotnine.data import *
import pandas as pd

def main():
    eje_1()
    eje_2()

def eje_1():
    x = bar.loc[bar.week_day.between(1,5),:]
    ggplot(aes(x='bill'),x)+geom_histogram()

def eje_2():
    ggplot(aes('orders','tip',color='gender'),bar)+geom_point()


if __name__ == "__main__":
    bar = pd.read_excel("Datasets\\bar.xlsx")
    main()