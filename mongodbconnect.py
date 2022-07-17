import pymongo


client = pymongo.MongoClient("mongodb+srv://jaimaa12:jaiMaata1!@rajeshnosql.zemtbb6.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "test",
    "email": "test@abc.com",
    "suname": "nkumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)