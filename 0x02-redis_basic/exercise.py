#!/usr/bin/env python3
"""Module that explores working with the Redis data structure store."""
import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    """Cache class definition."""

    def __init__(self) -> None:
        """Initialization of Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random uuid key and store the data in redis.

        Args:
            data (str | int | bytes | float): entry to store in redis.
        Return:
            str: the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve an element from the Redis data structure store.

        Args:
            key (str): id for the value in the Redis store.
            fn (Callable): function callable to convert the return
                type of the get method of redis.Redis() from bytes.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Parametrize Cache.get to string."""
        return self.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """Parametrize Cache.get to int."""
        value = self.get_str(key)
        try:
            value = int(value)
        except Exception:
            value = 0
        return value
