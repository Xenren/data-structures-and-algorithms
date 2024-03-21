from typing import Any


class DynamicArray:
    def __init__(self, items: Any) -> None:
        self.storage = []  # use built-in list for memory management
        self.size = 0
        self.capacity = len(items) * 2 if len(items) else 16
        if items:
            for item in items:
                self.append(item)

    def __repr__(self):
        pass

    def capacity(self) -> int:
        return self.capacity

    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def append(self, value: Any) -> None:
        self.storage[self.size] = value
        self.size += 1
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        return

    def resize(self, capacity: int) -> None:
        self.capacity = capacity
        return
