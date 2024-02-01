#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""

    def put(self, key, item):
        """Put method"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        return self.cache_data.get(key) if key else None
