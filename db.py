import pymongo

if __name__ == "__main__":
    print('Hello pymongo!')
    
    # connecting to client
    client = pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    
    #creating database
    db = client['cars_info']
    
    #creating collection
    collection = db['collection']
    
    # creating sample dict 
    dict = {'reg_number':'bcs-027','make':'toyota','owner_name':'berry','fines':False}
    collection.insert_one(dict)