import pandas as pd
import sqlalchemy


# PostgreSQL 접속 정보(db_engine)를 만든다.
def get_db_engine_from_postgres():
    # DB setting
    db_uri = 'postgresql://postgres:12345678@database-2.csebiuu6q8pc.ap-northeast-2.rds.amazonaws.com:5432/postgres'
    return sqlalchemy.create_engine(db_uri)


# create DataFrame from csv file
def create_dataframe_from_csv(file_name):
    # csv에서 데이터 임포트 all_medalists.csv
    return pd.read_csv(file_name)


# DataFrame 을 DB 에 insert
def insert_db_with_dataframe(dataframe, table_name, db_engine):
    dataframe.to_sql(table_name, db_engine, if_exists='replace', method='multi', index=False)


def main():
    db_engine = get_db_engine_from_postgres()
    df = create_dataframe_from_csv('../datasets/all_medalists.csv')
    insert_db_with_dataframe(df, 'all_medalists', db_engine)
    print('job completed..')


main()












