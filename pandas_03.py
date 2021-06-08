import pandas as pd

df = pd.read_csv('train.csv', index_col='PassengerId')

print(df['Survived'])
print(df[['Survived', 'Name', 'Age']])

print(df.Survived)

# 컬럼 생성
df['new_col'] = 0
print(df)
# 컬럼 삭제
del df['new_col']
print(df)

# 'famliy-size' 컬럼을 생성, Sipsp + Parch + 1
