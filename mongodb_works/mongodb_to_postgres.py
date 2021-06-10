# 몽고DB movies_sample.comments 데이터를 전체조회
# --> postgreSQL의 comments 테이블을 생성(자동생성)해서 데이터 insert

import pymongo
import sqlalchemy
import pandas as pd


def create_engine_postgresql():
    db_uri = 'postgresql://postgres:12345678@database-2.csebiuu6q8pc.ap-northeast-2.rds.amazonaws.com:5432/postgres'
    return sqlalchemy.create_engine(db_uri)


def create_connection_mongodb():
    return pymongo.MongoClient(
        "mongodb+srv://admin:1234qwer@cluster0.9lxgd.mongodb.net/?retryWrites=true&w=majority")


def find_comments_from_mongo(conn):
    comments = conn.movies_sample.comments
    return list(comments.find(
        {},
        {
            '_id': False,
            'movie_id': False
         }
    ))


def insert_to_postgres(engine, df):
    # 파이썬 리스트를 데이터프레임(판다스)으로 변환
    df.to_sql('comments_soongon', engine, if_exists='replace')


def main():

    # 데이터를 수집 (extract)
    conn = create_connection_mongodb()
    print('connection to mongodb completed..')
    comments_list = find_comments_from_mongo(conn)
    print('mongodb fetch ok..')

    # 데이터를 가공 (transformation)
    df = pd.DataFrame(comments_list)
    df['name'] = 'Le'

    # 데이터를 저장 (load)
    db_engine = create_engine_postgresql()
    print('posgtres connection ok..')
    insert_to_postgres(db_engine, df)
    print('dump to the postgres ok..')


main()