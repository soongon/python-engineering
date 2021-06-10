import pymongo
import sqlalchemy
import pandas as pd
import json
from pprint import pprint

# posgres titanic 데이터를 몽고DB movies_sample.titanic 에 로드

db_uri = 'postgresql://postgres:12345678@database-2.csebiuu6q8pc.ap-northeast-2.rds.amazonaws.com:5432/postgres'
db_engine = sqlalchemy.create_engine(db_uri)

# df = pd.read_sql('select * from titanic', db_engine)
df = pd.read_sql('titanic', db_engine)

titanic_json = json.loads(df.to_json(orient='records'))

conn = pymongo.MongoClient(
        "mongodb+srv://admin:1234qwer@cluster0.9lxgd.mongodb.net/?retryWrites=true&w=majority")
# 컬렉션 확보
titanic = conn.movies_sample.titanic

# list of dict (JSON)형태의 데이터를 파라미터로 전달
titanic.insert_many(titanic_json)
