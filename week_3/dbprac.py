from pymongo import MongoClient

client = MongoClient("mongodb+srv://lewigolski:1234@cluster0.1vcre.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

# doc = {
#     "name": "명수",
#     "age": 24,
# }

######### create ############
# db.users.insert_one(doc)

######### read ############
# all_users = list(db.users.find({}, {"_id": False}))
# print(all_users)

######### update ############
# db.users.update_one({"name": "명수"}, {"$set": {"age": 19}})

######### delete ############
# db.users.delete_one({"name": "명수"})
