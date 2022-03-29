"""
    Your task is to merge the given k sorted
    linked lists into one list and return
    the the new formed linked list class.
    Function Arguments:
        arr is a list containing the n linkedlist head pointers
        n is an integer dataue
    node class:
class Node:
    def __init__(self,value):
        self.data = value
        self.nxt = None
"""


from typing import Optional


def merge_k_lists(arr, k):
    """Merge k sorted linked list."""

    def merge_arr(arr, start, end):
        """Merge k sorted arrays"""
        if start == end:
            return arr[start]
        mid = start + (end - start) // 2
        left = merge_arr(arr, start, mid)
        right = merge_arr(arr, mid + 1, end)
        return merge(left, right)

    def merge(left, right):
        """Merge two sorted linked list."""
        head = Node(-1)
        temp = head
        while left is not None and right is not None:
            if left.data < right.data:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        while left is not None:
            temp.next = left
            left = left.next
            temp = temp.next
        while right is not None:
            temp.next = right
            right = right.next
            temp = temp.next
        return head.next

    if arr is None or k == 0:
        return None
    return merge_arr(arr, 0, k - 1)


class Node:
    """Node Class"""

    def __init__(self, data: int = 0, next: Optional["Node"] = None):
        self.data = data
        self.next = next

    def get_dataata(self):
        """Get the data of node."""
        return self.data

    def setData(self, data):
        """Set the data to the required node."""
        self.data = data


class LinkedList:
    """LinkedList class"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value: int):
        """Add node to linked list."""
        new_node = Node(data=value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def __str__(self):
        """Print linked list."""
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        return ""


def print_list(head: Node):
    """Print linked list."""
    walk = head
    while walk:
        print(walk.data, end=" ")
        walk = walk.next
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        line = [int(value) for value in input().strip().split()]
        heads = []
        IDX = 0
        for i in range(n):
            size = line[IDX]
            IDX += 1
            newList = LinkedList()
            for _ in range(size):
                newList.add(line[IDX])
                IDX += 1
            heads.append(newList.head)
        merged_list = merge_k_lists(heads, n)
        print_list(merged_list)
