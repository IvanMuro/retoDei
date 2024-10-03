import pandas as pd

df_csv = pd.read_csv('./data/reto.csv')
lst_json = df_csv.to_json(orient="records") 

print(lst_json)