import pandas as pd

df = pd.read_csv('train.csv')

print(type(df))
print(df.head())

df.to_excel('titanic.xlsx')
print('job completed..')
