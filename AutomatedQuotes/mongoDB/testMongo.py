
import pymongo
import certifi
ca = certifi.where()


client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
#db = client.test

db = client["AMQ"]
collection = db["Emails"]

#post ={"_id": 0,"name": "moshe",}
id = 1;
name ="rachelle"
post = {"_id": id,"name": name}
#collection.insert_one(post)
results = collection.find({"name": name})
counter =0
for result in results:
    counter = counter + 1
if counter == 0:
    collection.insert_one(post)
    id = id+1
    
#QV9BcLxtJqrInZB4  ,tlsCaFile=ca