import pandas as pd
import sqlalchemy

db_uri = 'postgresql://postgres:12345678@database-2.csebiuu6q8pc.ap-northeast-2.rds.amazonaws.com:5432/postgres'
db_engine = sqlalchemy.create_engine(db_uri)

query = 'select * from all_medalists where "NOC" = \'KOR\''

df = pd.read_sql(query, db_engine)

df.to_sql('medalists_kor', db_engine, if_exists='replace')
print('job ok..')
