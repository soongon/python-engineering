import pymongo

conn = pymongo.MongoClient(
    "mongodb+srv://admin:1234qwer@cluster0.9lxgd.mongodb.net/?retryWrites=true&w=majority")

# sample_mflix.comments 에서 데이터를 조회 --> list of dict
comments = conn.sample_mflix.comments
search_result = list(comments.find({
    'name': 'Andrea Le'
}))

# movies_sample.comments 에서 insert
target_col = conn.movies_sample.comments
insert_result = target_col.insert_many(search_result)

print(insert_result)
conn.close()