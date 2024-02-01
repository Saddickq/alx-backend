#!/usr/bin/env python3
"""FIFOCache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""
    def __init__(self):
        """init method"""
        self.usedKeys = []
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[self.usedKeys[0]]
                print(f"DISCARD: {self.usedKeys[0]}")
                self.usedKeys.pop(0)
            self.cache_data[key] = item
            self.usedKeys.append(key)

    def get(self, key):
        """get method"""
        if key and self.cache_data.get(key):
            self.usedKeys.remove(key)
            self.usedKeys.append(key)
            return self.cache_data.get(key)
