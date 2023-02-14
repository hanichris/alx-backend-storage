#!/usr/bin/env python3
"""Update the document with the given name field."""


def update_topics(mongo_collection, name, topics):
    """Change the topics of a school document based on the name.

    Args:
        mongo_collection (MongoClient): pymongo collection object.
        name (str): school name to update.
        topics (list[str]): list of topics approached in the school.
    """
    query = {"name": name}
    update_value = {"$set": {"topics": topics}}
    mongo_collection.update_one(query, update_value)
