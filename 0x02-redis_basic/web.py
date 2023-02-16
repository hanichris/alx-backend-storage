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
        url = args[0]
        key = f"count:{url}"
        r.incr(key)
        cached = r.get(f'url')
        if cached:
            return cached.decode("utf-8")
        r.setex(f'{url}', 10, func(url))
        return func(*args, **kwargs)
    return wrapper


@url_visits
def get_page(url: str) -> str:
    """Obtain HTML content of a page and return it."""
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    get_page(url)
