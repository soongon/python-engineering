# 몽고DB movies_sample.comments 데이터를 전체조회
# --> postgreSQL의 comments 테이블을 생성(자동생성)해서 데이터 insert

import pymongo
import sqlalchemy


def create_engine_postgresql():
    db_uri = 'postgresql://postgres:12345678@database-2.csebiuu6q8pc.ap-northeast-2.rds.amazonaws.com:5432/postgres'
    return sqlalchemy.create_engine(db_uri)


def create_connection_mongodb():
    return pymongo.MongoClient(
        "mongodb+srv://admin:1234qwer@cluster0.9lxgd.mongodb.net/?retryWrites=true&w=majority")


def find_comments_from_mongo(conn):
    comments = conn.movies_sample.comments
    return list(comments.find())


def insert_to_postgres(engine, comments):
    print(comments)


def main():
    conn = create_connection_mongodb()
    comments_list = find_comments_from_mongo(conn)
    db_engine = create_engine_postgresql()
    insert_to_postgres(db_engine, comments_list)


main()