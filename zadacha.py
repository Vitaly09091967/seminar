Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

df = pd.read_csv("sample_data/california_housing_train.csv")
min_pop = df["population"].min()
max_households = df.loc[df["population"] == min_pop, "households"].max()
print("Максимальное количество домохозяйств в зоне с минимальным населением ({}): {}".format(min_pop, max_households))
