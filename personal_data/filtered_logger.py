#!/usr/bin/env python3
"""
Filter datum logger
"""

import re

def filter_datum(fields, redaction, message, separator):
    """
    returns the log message obfuscated
    """
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator, message)
    return message
