from dataclasses import dataclass, field
from typing import Any, Optional, TypeVar, Generic

T = TypeVar("T")  # Generic type placeholder


@dataclass
class Node(Generic[T]):
    """
    A generic node for singly or doubly linked lists.

    Attributes:
        data (T): The data stored in the node.
        next_node (Optional[Node[T]]): The next node reference.
        previous_node Optional['Node[T]']: The previous node reference
    """

    data: Any = T
    next_node: Optional["Node[T]"] = field(default=None, repr=False)
    previous_node: Optional["Node[T]"] = field(
        default=None, repr=False
    )  # Use only for doubly-linked lists

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"
