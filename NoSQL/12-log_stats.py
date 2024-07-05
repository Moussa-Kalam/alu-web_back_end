#!/usr/bin/env python3
"""Log stats module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    num_logs = db.count_documents({})
    print(f"{num_logs} logs")

    get = db.count_documents({'method': 'GET'})
    post = db.count_documents({'method': 'POST'})
    put = db.count_documents({'method': 'PUT'})
    patch = db.count_documents({'method': 'PATCH'})
    delete = db.count_documents({'method': 'DELETE'})

    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")

    status = db.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status} status check")
