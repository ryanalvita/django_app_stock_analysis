import json

from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

from utils import get_mongo_collection


def get_stock_data(request, stock, report_type, statement_type):
    collection = get_mongo_collection(collection_name=statement_type)
    data = collection.find_one({"stock_code": stock})[report_type]

    return HttpResponse(json.dumps(data), content_type="application/json")
