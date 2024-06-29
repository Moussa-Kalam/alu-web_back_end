#!/usr/bin/env python3
""" Redis instance """
import redis
import uuid
from typing import Union, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Save the call history of different function calls """

    @functools.wraps(method)
    def wrapper(self, *args):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output

    return wrapper


def replay(method: Callable) -> None:
    """display the history of calls of a particular function"""

    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name)
    inputs = r.lrange(f"{method_name}:inputs", 0, -1)
    outputs = r.lrange(f"{method_name}:outputs", 0, -1)
    print(f"{method_name} was called {count} times:")
    for i, o in zip(inputs, outputs):
        print(f"{method_name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


def replay(func):
    """ Display the history of calls """

    cache = func.__self__
    red = cache._redis
    call_inputs = func.__qualname__ + ":inputs"
    call_outputs = func.__qualname__ + ":outputs"
    items = zip(red.lrange(call_inputs, 0, -1),
                red.lrange(call_outputs, 0, -1))
    print(f"{func.__qualname__} was called {red.llen(call_inputs)} times:")
    for k, v in items:
        k = k.decode('utf-8')
        v = v.decode('utf-8')
        print(f"{func.__qualname__}(*{k}) -> {v}")


class Cache:
    """ Redis cache """

    def __init__(self):
        """ Initialize redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate random key and store data in redis """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: callable = None):
        """ Get data from redis and optionally transform it using fn """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Get data from redis and transform it to string """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Get data from redis and transform it to int """
        return self.get(key, int)
