from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("localhost", 27017)

database = client["Century"]

data = {"Author": "Berkay Yavuz",
        "About": "Python Mongodb",
        "Tags": ["mongodb", "python", "pymongo"]}

collection = database.Archive

result = collection.insert_one(data)

print("First inserted data's key is {}".format(result.inserted_id))
print(database.list_collection_names)

data1 = {"Author": "Emmanuel Kens",
         "About": "Artificial Intelligence",
         "Tags": ["Deep learning", "Machine learning"]}

data2 = {"Author": "Daniel Kimeli",
         "About": "Web Development",
         "Tags": ["HTML", "CSS", "Javascript"]}

result = collection.insert_many([data1, data2])

print("The new inserted datas's key is {}".format(result.inserted_ids))

print(collection.find_one()) # Collection'ın içindeki ilk veri

for data in collection.find(): # Tüm veriler
    print(data)

def get(post_id): 

    document = client.Century.Archive.find_one({"_id": ObjectId(post_id)}) # X Id'li veri
    return document

returned = get('5deaa75b41932420f411d576')
print("5deaa75b41932420f411d576'Id'li döküman: {}".format(returned))