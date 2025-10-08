print("Hello World")
import pandas as pd
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)

data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

dat= pd.date_range('2021-05-01','2021-05-12')
print(dat)

my_series = pd.Series([2, 4, 6, 8, 10])
my_series = my_series.apply(lambda x: x / 2)
print(my_series)