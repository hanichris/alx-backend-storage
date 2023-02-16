#!/usr/bin/env python3
"""Implement an expiring web cache and tracker"""
import functools
import redis
import requests
from typing import Callable


r = redis.Redis()

def url_visits(func: Callable) -> Callable:
    """Define a decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        key = f"count:{args[0]}"
        r.incr(key)
        r.expire(key, 10)
        return func(*args, **kwargs)
    return wrapper

@url_visits
def get_page(url: str) -> str:
    """Obtain HTML content of a page and return it."""
    r = requests.get(url)
    return r.text()

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    get_page(url)
    print(f"no of vists: {r.get(f'count:{url}')}")
    get_page(url)
    get_page(url)
    get_page(url)
    print(f"no of vists: {r.get(f'count:{url}')}")
