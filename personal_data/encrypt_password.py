#!/usr/bin/env python3
""" encrypting password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypt password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())