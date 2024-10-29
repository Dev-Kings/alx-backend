# 0x01. Caching

## Back-end Development

### Project Overview
This project explores various caching algorithms and strategies, aimed at enhancing backend performance. You will learn how caching systems work, the purposes they serve, and the limitations they face.

---

### Background Context
Caching is a fundamental concept in software engineering, particularly in back-end development, where data retrieval speed and efficiency can significantly impact performance. Through this project, you will gain a practical understanding of various caching policies and their applications.

---

## Resources

1. [Cache Replacement Policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies)
2. [Cache Replacement Policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies)
3. [Cache Replacement Policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies)
4. [Cache Replacement Policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies)
5. [Cache Replacement Policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies)

---

## Learning Objectives

### General Concepts
- **Caching System:** Understand what a caching system is and why it's important in back-end development.
- **FIFO (First-In, First-Out):** Learn the FIFO policy and how it manages cache replacement.
- **LIFO (Last-In, First-Out):** Explore the LIFO policy and its approach to cache management.
- **LRU (Least Recently Used):** Understand the LRU policy and how it prioritizes data based on recent usage.
- **MRU (Most Recently Used):** Learn about the MRU policy and its caching methodology.
- **LFU (Least Frequently Used):** Understand how LFU operates by prioritizing data based on usage frequency.
- **Purpose of a Caching System:** Learn the benefits of caching, including improved response time and reduced server load.
- **Limitations of Caching Systems:** Identify the constraints that affect caching, such as storage limits and cache invalidation issues.

---
## 0. Basic dictionary

### Module: `0-basic_cache.py`
Defines the `BasicCache` class, which is a basic caching system that inherits from `BaseCaching`.

---

## BasicCache Class

### Description
The `BasicCache` class provides a caching system that stores key-value pairs without any limits on the number of items stored.

### Methods
- `put(key, item)`: Adds the `item` to `self.cache_data` using `key`. If `key` or `item` is `None`, the method does nothing.
- `get(key)`: Retrieves the value associated with `key` from `self.cache_data`. Returns `None` if `key` is `None` or does not exist.

### Example Usage
```python
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))  # Outputs: Hello
print(my_cache.get("B"))  # Outputs: World
print(my_cache.get("C"))  # Outputs: Holberton
print(my_cache.get("D"))  # Outputs: None
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))  # Outputs: Street
