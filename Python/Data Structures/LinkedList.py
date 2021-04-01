class LinkedList:
    class Node:
        __slots__ = "data", "next"

        def __init__(self, data, next) -> None:
            self.data = data
            self.next = next

    def __init__(self) -> None:
        self.head = None
        self
