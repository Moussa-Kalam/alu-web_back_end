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
