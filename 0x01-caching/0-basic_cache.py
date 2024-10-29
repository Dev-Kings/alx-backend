#!/usr/bin/env python3
"""
This module contains the BasicCache class, a basic caching system
without any size limit, which inherits from BaseCaching.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system
    with no limit.
    """

    def put(self, key, item):
        """
        Assigns the item to the cache dictionary using the key.
        Args:
            key (str): Key for the item.
            item (any): The item to cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in the cache linked to the provided key.
        Args:
            key (str): Key for the item to retrieve.
        Returns:
            The value linked to key if key is in cache_data; otherwise, None.
        """
        return (self.cache_data.get(key, None))
