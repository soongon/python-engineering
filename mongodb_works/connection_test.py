import pymongo

conn = pymongo.MongoClient(
    "mongodb+srv://admin:1234qwer@cluster0.9lxgd.mongodb.net/python_test?retryWrites=true&w=majority")

print(conn)
