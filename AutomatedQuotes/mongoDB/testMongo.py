
import pymongo
import certifi
ca = certifi.where()


client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
#db = client.test

db = client["Stocks"]
collection = db["Users"]



t = collection.distinct("User")
for i in t:
    count = collection.find({"User":i},{"_id":0})
    
    for j in count:
        print(j)
    #print(f"{i} count = {count}")
print(t.count(t))