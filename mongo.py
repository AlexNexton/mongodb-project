import os
import pymongo
if os.path.exists("env.py"):
    import env

MON_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to mongoDB: %s") % e


conn = mongo_connect(MON_URI)

coll = conn[DATABASE][COLLECTION]

new_doc = {"first":"douglas", "last":"adams","dob":"10/11/1945","hair_color": "grey","occupation":"writer","nationality":"british"}




documents = coll.find({"first":"douglas"})

for doc in documents:
    print(doc)