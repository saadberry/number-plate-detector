import pymongo
client = pymongo.MongoClient("mongodb+srv://admin:123@cluster0.yhetv.mongodb.net/car_info?retryWrites=true&w=majority")
db = client.car_info

col = db['details']
# print(client.list_database_names())
# print(db.list_collection_names())

car_info = [{"numberplate":"abc-123","name":"abdu rozik","make":"tesla","model":2020},
            {"numberplate":"def-456","name":"maaz jaaz","make":"toyota","model":2019}]
x = col.insert_many(car_info)
# print('id of inserted data is:',x)