from typing import Any


def hash_key(key: Any) -> Any:
    """
    If the key is mutable, it is converted into a tuple to make it hashable.
    """
    if isinstance(key,  (list, dict, set)):
        return tuple(key)
    else:
        return key


class LruCache:

    def __init__(self, size: int):
        """
        param size: size for cache.
        attribute __cache: dict to store arithmetic operations (keys: operations, values: results).
        attribute __order: order of keys, index 0 Least Recently used, index n-1 Most Recently used.
        """

        self.__size = size
        self.__cache = {}
        self.__order = []

    @property
    # property to write <catch> instead of <__cache>.
    def cache(self):
        return self.__cache

    def put(self, key: Any, value: Any):
        """
        :param key: arithmetic operations.
        :param value: results.
        method to store key: arithmetic operations and value: results.
        if user tried to exceed the size of cache ,then pop the key and the value of the Least Recently used element.
        both in cache and order and insert the new element into n-1 index(tail) in order, also insert into cache.
        if we got additional space, then store key and value in cache and order(as last element).
        """
        hashed_key = hash_key(key)

        if len(self.cache) == self.__size:
            removed_key = self.__order.pop(0)
            self.cache.pop(removed_key)

        self.cache[hashed_key] = value
        self.__order.append(key)

    def get(self, key: Any) -> Any:
        """
        method to get value of specific key.
        getting a value of a key make this pair as Most Recently used, so we need to update order and replace them.
        in n-1 index in order.
        """
        if key not in self.__cache:
            return False
        else:
            self.__order.remove(key)
            self.__order.append(key)
            return self.cache.get(key)

    def __str__(self):
        """
        friendly user text presentation of each inserted pair in cache.
        """
        s_cache: str = ""
        for key, value in self.cache.items():
            s_cache += f"{key} : {value}\n"

        return s_cache
