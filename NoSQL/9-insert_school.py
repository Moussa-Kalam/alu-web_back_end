#!/usr/bin/env python3
"""insert a document in a collection"""

def insert_school(mongo_collection, **kwargs):
    """insert a document in a collection"""
    return mongo_collection.insert_one(kwargs).inserted_id

