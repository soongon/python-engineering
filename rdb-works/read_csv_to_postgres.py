import pandas as pd
import sqlalchemy

DB_URI = 'postgresql://postgres:12345678@database-2.csebiuu6q8pc.ap-northeast-2.rds.amazonaws.com:5432/postgres'

# 타이타닉 데이터 CSV 읽어서 데이터프레임으로 만든다.
titanic_df = pd.read_csv('../train.csv')

# 데이터베이스 접속 정보를 만든다.
db_engine = sqlalchemy.create_engine(DB_URI)

# 데이터프레임을 데이터베이스 'titanic' 테이블에 insert.
titanic_df.to_sql('titanic', db_engine, if_exists='replace')

print('job ok..')
