import pymongo
import pprint

conn = pymongo.MongoClient(
    "mongodb+srv://admin:1234qwer@cluster0.9lxgd.mongodb.net/?retryWrites=true&w=majority")

actors = conn.movies_sample.actors

actor = {
    'name': '정우성',
    'age': 50,
    'gender': 'male'
}

result = actors.insert_one(actor)

print(result)
conn.close()