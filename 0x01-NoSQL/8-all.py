#!/usr/bin/env python3
"""Function to list all the documents in a MongoDB collection."""


def list_all(mongo_collection):
    """List all documents in a collection.

    Args:
        mongo_collection (object): pymongo collection object.
    Returns:
        list: all documents in the collection.
    """
    return mongo_collection.find()
