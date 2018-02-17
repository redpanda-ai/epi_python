class ListNode:
    """This class is esentially a singly linked list, provided in the book"""
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def print_list(L):
    """basic function to display the list"""
    K = L
    arr = []
    while K:
        arr.append(str(K.data))
        K = K.next
    print("(head) " + " -> ".join(arr) + " (tail)")


def get_list(my_array):
    """returns a singly linked list built from an array"""
    head = None
    tail = None
    for item in my_array:
        if not head:
            head = ListNode(data=item)
            tail = head
        else:
            tail.next = ListNode(data=item)
            tail = tail.next
    return head
