#!/usr/bin/env python3
"""Provide some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_col = client.logs.nginx

    get_num = nginx_col.count_documents({'method': 'GET'})
    post_num = nginx_col.count_documents({'method': 'POST'})
    put_num = nginx_col.count_documents({'method': 'PUT'})
    patch_num = nginx_col.count_documents({'method': 'PATCH'})
    del_num = nginx_col.count_documents({'method': 'DELETE'})
    stat_num = nginx_col.count_documents({'method': 'GET',
                                          'path': '/status'})

    print(f"{nginx_col.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_num}")
    print(f"\tmethod POST: {post_num}")
    print(f"\tmethod PUT: {put_num}")
    print(f"\tmethod PATCH: {patch_num}")
    print(f"\tmethod DELETE: {del_num}")
    print(f"{stat_num} status check")
