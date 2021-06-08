import pandas as pd

df = pd.read_csv('train.csv', index_col='PassengerId')

print(df.info())

print(df.columns)