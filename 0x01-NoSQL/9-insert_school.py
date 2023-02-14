#!/usr/bin/env python3
"""Insert a new document into a collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document into a collection based on kwargs.

    Args:
        mongo_collection (MongoClient): pymongo collection object.
        kwargs (dict): key-word arguments.
    Return:
        str: unique id `_id`.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
