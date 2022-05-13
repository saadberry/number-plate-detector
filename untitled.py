import sys
import pymongo
# import dns
import datetime
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://saadberry:4O51nCUhbx8blgZk@cluster0.zqfl4.mongodb.net/test?retryWrites=true&w=majority")
db = cluster['test']
col = db['test1']
x = {"name":"saad"}
collection.insert_one(x)
print(db.list_collection_names())
# db.client.hehe
# people=db.people
# personDocument = {
#   "name": { "first": "Alan", "last": "Turing" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }  
# people.insert_one(personDocument)

# if __name__ == "__main__":
#     print('Hello pymongo!')
    
#     # connecting to client
#     client = pymongo.MongoClient('mongodb://localhost:27017')
#     print(client)
    
#     #creating database
#     db = client['cars_info']
    

#creating collection
    # collection = db['collection']
    
    # creating sample dict 
    # dict = {'reg_number':'bcs-027','make':'toyota','owner_name':'berry','fines':False}
    # collection.insert_one(dict)
    
    
    # mongodb+srv://saadberry:@test.zqfl4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
    


