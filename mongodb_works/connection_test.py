import pymongo
import pprint

conn = pymongo.MongoClient(
    "mongodb+srv://admin:1234qwer@cluster0.9lxgd.mongodb.net/?retryWrites=true&w=majority")

comments = conn.sample_mflix.comments

# 데이터 조회 (find)
result = list(comments.find({
    'name': 'Andrea Le'
}))

pprint.pprint(result[1]['email'])
conn.close()
