from pymongo import MongoClient


def get_mongo_collection(collection_name):
    client = MongoClient(
        "mongodb+srv://mongo:KgWIfb4AzqkTyDXb@stockanalysis.f30kw8z.mongodb.net/?retryWrites=true&w=majority"
    )
    db = client["stockbit_data"]
    collection = db[collection_name]

    return collection
