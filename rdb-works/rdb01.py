
import pandas as pd

df = pd.read_csv('../train.csv')

print(df.head())

df.to_excel('titanic.xlsx')

print('job ok..')