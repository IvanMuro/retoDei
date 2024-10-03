import pandas as pd
pd.set_option('display.max_rows', None) #Show all columns when printing DataFrame

df_json = pd.read_json('./data/reto.json', orient='split')
dist_sum = df_json.groupby('Matricula')['Distance'].sum()
print(dist_sum)