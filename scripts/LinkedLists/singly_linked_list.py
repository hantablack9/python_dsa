from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Iterator, Union, List
from node import Node

T = TypeVar("T")


@dataclass
class SinglyLinkedList(Generic[T]):
    head: Optional["Node[T]"] = None

    def insert_at_head(self, data: T) -> None:
        new_node = Node(data=data, next_node=self.head)
        self.head = new_node

    def length(self) -> int:
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next_node
        return counter

    def __len__(self) -> int:
        return self.length()

    def last_node(self) -> Optional["Node[T]"]:
        current = self.head

        if not current:
            return None

        while current.next_node:
            current = current.next_node
        return current

    def append(self, data: T) -> str:
        new_node = Node(data=data)
        tail = self.last_node()
        if tail:
            tail.next_node = new_node
        return "Success: Appended at the tail"

    def search(
        self, data: T, first_only: bool = True, return_position: bool = True
    ) -> Union[int, bool, List[int], None]:
        index = 0
        positions = []
        current = self.head

        while current:
            if current.data == data:
                if first_only:
                    return index if return_position else True
                else:
                    positions.append(index)

            index += 1
            current = current.next_node

        if first_only:
            return None if return_position else False
        return positions if return_position else bool(positions)

    def delete(self, data: T) -> None:
        pass

    def reverse(self) -> None:
        pass

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def __repr__(self) -> str:
        values = [str(data) for data in self]
        return "->".join(values) + "None"
