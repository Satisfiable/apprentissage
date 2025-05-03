from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("localhost", 27017)
database = client["Century"]

collection = database.Archive

for data in collection.find({}, {"_id": 0, "Author": 1}): # Belli değerleri alma. "_id" = 0 ise diğer değerler 1 olmak zorunda! "_id" hariç diğer değerler 0 ve 1 değerlerini aynı anda alamazlar.
    for i in data.values():
        if (i == "Berkay Yavuz"):
            print(i)

document = collection.find().sort("Author", 1) # 1 or -1

for i in document:
    print(i)

print("******")

query = {"Author": "Berkay Yavuz"}
new_author = {"$set": {"Author": "Sara"}}
collection.update_one(query, new_author)

for i in collection.find():
    print(i)

print("******")

limited_result = collection.find().limit(1)

for i in limited_result:
    print(i)

print("******")

collection.delete_one({"_id": ObjectId("5deaa6fcb0f60992eb4465a3")})

for i in collection.find():
    print(i)

result = collection.delete_many({}) # Tüm verileri silmek.
print(result.deleted_count, " datas deleted!")

collection.drop() # Collection silmek.





