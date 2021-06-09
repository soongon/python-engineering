import pandas as pd

df = pd.read_csv('../datasets/dogs.csv')

agg = df[['Height(cm)', 'Weight(kg)']].min()

print(agg)
