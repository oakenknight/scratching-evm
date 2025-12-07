from storage import KeyValue

class TStorage(KeyValue):
    def __init__(self):
        super().__init__()
        self.cache = []

    def load(self, key):
        warm = True if key in self.cache else False
        if not warm:
            self.cache.append(key)
        if key not in self.storage:
            return 0x00
        return warm, super().load(key)
    def store(self, key, value):
        warm = key in self.cache
        if not warm:
            self.cache.append(key)
        self.storage[key] = value
        return warm
    
    def reset(self):
        self.storage.clear()
        self.cache.clear()