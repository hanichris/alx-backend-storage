#!/usr/bin/env python3
"""Using an aggregation pipeline."""


def top_students(mongo_collection):
    """Return all the students sorted by average score.

    Args:
        mongo_collection (MongoClient): pymongo collection object.
    Return:
        cursor.
    """
    pipeline = [
            {
                "$project":
                {
                    "name": 1,
                    "averageScore": {"$avg": "$topics.score"}}
            },
            {"$sort": {"averageScore": -1}}
            ]
    return mongo_collection.aggregate(pipeline)
