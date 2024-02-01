#!/usr/bin/env python3
"""FIFOCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""
    def __init__(self):
        """initialisation method"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                removed = sorted(self.cache_data)[0]
                self.cache_data.pop(removed)
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        return self.cache_data.get(key) if key else None
