#!/usr/bin/env python3
""" Redis instance """
import redis
import uuid
from typing import Union


class Cache:
    """ Redis cache """

    def __init__(self):
        """ Initialize redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate random key and store data in redis """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

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
