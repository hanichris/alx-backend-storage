#!/usr/bin/env python3
"""Module that explores working with the Redis data structure store."""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class definition."""

    def __init__(self) -> None:
        """Initialization of Cache class."""
        _redis = redis.Redis()
        _redis.flushdb()

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