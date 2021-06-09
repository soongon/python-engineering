import pandas as pd
import sqlalchemy

query = 'select * from users'
table_name = 'users'

# DB 접속 엔진을 만든다.
db_uri = 'postgresql://postgres:12345678@database-2.csebiuu6q8pc.ap-northeast-2.rds.amazonaws.com:5432/postgres'
db_engine = sqlalchemy.create_engine(db_uri)

# postgreSQL 에서 데이터를 읽어 들입니다.
df = pd.read_sql(table_name, db_engine)

# df(데이터프레임)을 관계형 DB 특정 테이블에 인서트..
df.to_sql('users002', db_engine, if_exists='append', index=False)

print(df.head())