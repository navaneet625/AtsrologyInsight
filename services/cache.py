import time

class SimpleCache:
    def __init__(self):
        self.data = {}

    def set(self, key, value, ttl=300):
        self.data[key] = (value, time.time() + ttl)

    def get(self, key):
        item = self.data.get(key)
        if not item:
            return None
        val, exp = item
        if time.time() > exp:
            del self.data[key]
            return None
        return val
