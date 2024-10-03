import pandas as pd
pd.set_option('display.max_rows', None) #Show all columns when printing DataFrame

df_csv = pd.read_csv('./data/reto.csv')
print(df_csv)