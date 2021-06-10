import pandas as pd

df = pd.read_csv('../train.csv')

print(df.groupby(['Pclass', 'Sex'])['Survived'].agg(['mean', 'sum']))


