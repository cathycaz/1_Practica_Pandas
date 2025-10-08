print("Hello World")
import pandas as pd
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)

data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

dat= pd.date_range('2021-05-01','2021-05-12')
print(dat)

my_series = pd.Series([2, 4, 6, 8, 10])
my_serie_2 = my_series /2
print(my_serie_2)
my_series = my_series.apply(lambda x: x / 2)
print(my_series)

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=["Brand", "Model", "Color"])
print(df)


data_nueva = [["Toyota", "Corolla", "Blue"], 
              ["Ford", "K", "Yellow"], 
              ["Porsche", "Cayenne", "White"],
              ["Tesla", "Model S", "Red"]]

df1 = pd.DataFrame(data_nueva, columns=["brand", "model", "color"])
print(df1)

"""nuevo_dato = {
        "Brand": "Tesla", 
        "Model": "Model S",
        "Color": "Red"
}
df.loc[len(df)] = nuevo_dato

print(df)"""

# 05.2
data_frame_nueva= pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame_nueva.iloc[133,6]) # Imprime el valor en la fila 133 y columna 6
print(data_frame_nueva.iloc[0:5,0:3]) # Imprime las primeras 5 filas y las primeras 3 columnas
print(data_frame_nueva.head(3)) # Imprime las primeras 3 filas del DataFrame
print(data_frame_nueva.tail(3)) # Imprime las últimas 3 filas del DataFrame

print(data_frame_nueva[['Name', 'Type 1']][0:10]) # Imprime las columnas 'Name' y 'Type 1'
print(data_frame_nueva.loc[data_frame_nueva['Attack']>80]) # Imprime la columna 'Attack'
