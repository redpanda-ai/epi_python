class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False


class BinaryTreeNodeParentPointer:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False


def tree_traversal(root, traversal_order, height=0, leaf_heights={}):
    """Recursive function that passes the heights, and a dictionary of lowest
    and highest leaf heights into each recursive call."""

    def status(x):
        print("{}: {}, is_leaf: {}, height: {}".format(
            traversal_order, x, root.is_leaf(), height))

    if root:
        if root.is_leaf():
            if not leaf_heights:
                leaf_heights["lowest"] = height
                leaf_heights["highest"] = height
            elif leaf_heights["lowest"] > height:
                leaf_heights["lowest"] = height
            elif leaf_heights["highest"] < height:
                leaf_heights["highest"] = height

        if traversal_order == "Preorder":
            status(root.data)
        tree_traversal(
            root.left, traversal_order, height=height+1,
            leaf_heights=leaf_heights)
        if traversal_order == "Inorder":
            status(root.data)
        tree_traversal(
            root.right, traversal_order, height=height+1,
            leaf_heights=leaf_heights)
        if traversal_order == "Postorder":
            status(root.data)
        if height == 0:
            if leaf_heights["highest"] - leaf_heights["lowest"] > 1:
                print("This tree is not height balanced")
            else:
                print("This tree is height balanced")
            print(leaf_heights)


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
