import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "Celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MondoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# Add multiple lines of data to MondoDB
new_docs = [{
    "first": "terry",
    "last": "pratchett",
    "dob": "28/04/1948",
    "gender": "m",
    "hair_color": "not much",
    "occupation": "writer",
    "nationality": "british",
}, {
    "first": "george",
    "last": "rr martin",
    "dob": "20/09/1948",
    "gender": "m",
    "hair_color": "white",
    "occupation": "writer",
    "nationality": "american",
}]

# Function to insert docs to database.
# Other Functions: coll.find(), coll.update_one(),
# coll.update_many(), coll.remove()
# coll.update_many({"gender": "m"}, {$set: {"hair_color": "blonde"}})
#  - Sets all Males to blonde hair
coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)
