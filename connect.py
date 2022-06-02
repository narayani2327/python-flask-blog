from pymongo import MongoClient
client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
mydatabase = client.cars
mycollection = mydatabase.carnames
record = {
    "title": 'Narayani', 
    "description": 'MongoDB is no SQL database', 
    "tags": ['mongodb', 'NoSQL'], 
    "viewers": 105 
} 
rec = mycollection.insert_one(record)
for i in mycollection.find({"title": 'MongoDB and Python'}):
    print(i)