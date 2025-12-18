from collections import deque
from typing import Any


class Stack:
    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


if __name__ == "__main__":
    s = Stack()
    print(f"Стек пуст? {s.is_empty()}")
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Размер стека после push: {len(s)}")
    print(f"Верхний элемент (peek): {s.peek()}")
    print(f"pop(): {s.pop()}")
    print(f"Верхний элемент после pop: {s.peek()}")
    print(f"Стек пуст? {s.is_empty()}")
