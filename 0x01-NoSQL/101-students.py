#!/usr/bin/env python3
"""Using an aggregation pipeline."""
from bson.son import SON


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
            {"$sort": SON([("averageScore", -1), ("_id", -1)])}
            ]
    return mongo_collection.aggregate(pipeline)
