import time
from typing import Optional

class SimpleCache:
    def __init__(self):
        self._data = {}

    def set(self, key: str, value, ttl: int = 300) -> None:
        self._data[key] = (value, time.time() + ttl)

    def get(self, key: str):
        item = self._data.get(key)
        if not item:
            return None
        value, expires_at = item
        if time.time() > expires_at:
            del self._data[key]
            return None
        return value
    
cache = SimpleCache()
