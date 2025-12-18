from typing import Any, Iterator


class Node:
    def __init__(self, value: Any, next: "Node | None" = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node

        if self._size == 0:
            self.tail = new_node

        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        if idx == 0:
            assert self.head is not None
            self.head = self.head.next
            self._size -= 1
            if self._size == 0:
                self.tail = None
            return

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        assert current.next is not None
        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(map(str, self))}])"


if __name__ == "__main__":
    lst = SinglyLinkedList()

    print(f"Длина нашего односвязного списка : {len(lst)}")

    lst.append(0)
    lst.append(1)
    lst.append(2)
    print(f"Наша нынешняя длина списка после добавления элементов : {len(lst)}")
    print(f"Односвязанный список : [{', '.join(map(str, lst))}]")

    lst.insert(1, 0.5)
    print(f"Длина списка после добавления на 1 индекс числа 0.5 : {len(lst)}")
    print(f"Односвязанный список : [{', '.join(map(str, lst))}]")

    lst.append(52)
    print(
        "Односвязанный список после добавления числа в конец : "
        f"[{', '.join(map(str, lst))}]"
    )

    current = lst.head
    chain_parts = []
    while current is not None:
        chain_parts.append(f"[{current.value}]")
        current = current.next
    chain_str = " -> ".join(chain_parts) + " -> None"
    print(chain_str)
