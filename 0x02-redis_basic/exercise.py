#!/usr/bin/env python3
"""Module that explores working with the Redis data structure store."""
import functools
import redis
import uuid
from typing import Callable, Optional, Union


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs of a function."""
    key = method.__qualname__
    inputs = f"{key}:inputs"
    outputs = f"{key}:outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function."""
        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Count calls to the methods of class Cache."""
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function."""
        self._redis.incr(key)
        return method(self, *args, *kwargs)
    return wrapper


class Cache:
    """Cache class definition."""

    def __init__(self) -> None:
        """Initialization of Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
            fn: Optional[Callable] = None) -> Union[bytes, str, int, float]:
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
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """Parametrize Cache.get to int."""
        value = self._redis.get(key)
        try:
            value = int(value.decode("uft-8"))
        except Exception:
            value = 0
        return value


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function."""
    key = method.__qualname__
    inputs = f"{key}:inputs"
    outputs = f"{key}:outputs"
    _redis = method.__self__._redis

    count = _redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    input_list = _redis.lrange(inputs, 0, -1)
    output_list = _redis.lrange(outputs, 0, -1)
    for arg, res in zip(input_list, output_list):
        arg, res = arg.decode("utf-8"), res.decode("utf-8")
        print(f"{key}(*{arg}) -> {res}")
