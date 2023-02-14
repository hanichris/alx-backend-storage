#!/usr/bin/env python3
"""Return all the schools with a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic.

    Args:
        mongo_collection (MongoClient): pymongo collection object.
        topic (str): topic to be searched for.
    Return:
        list.
    """
    return mongo_collection.find({"topics": topic})
