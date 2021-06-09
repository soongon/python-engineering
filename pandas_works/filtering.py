# 메달리스트 데이터를 읽어서 한국 KOR 메달리스트만 조회(filtering)

import pandas as pd

df = pd.read_csv('../datasets/all_medalists.csv')

new_df = df.loc[(df['City'] == 'Beijing') & (df['NOC'] == 'KOR')]

print(new_df)