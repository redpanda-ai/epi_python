import sys, random
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def __repr__(self):
        l = "" if self.left is None else self.left.data
        r = "" if self.right is None else self.right.data
        return "(data: {}, left: {}, right: {})".format(
            self.data, l, r)


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
            print(root.data)
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

def binary_tree_from_preorder_inorder(preorder, inorder):
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end].
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
                                                 inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # Recursively builds the left subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1, preorder_start + 1 + left_subtree_size,
                inorder_start, root_inorder_idx),
            # Recursively builds the right subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size, preorder_end,
                root_inorder_idx + 1, inorder_end))
    return binary_tree_from_preorder_inorder_helper(
        0, len(preorder), 0, len(inorder))

def simple_test():
    res = binary_tree_from_preorder_inorder([1], [1])
    assert res.data == 1

    res = binary_tree_from_preorder_inorder([2, 1], [1, 2])
    assert res.data == 2 and res.left.data == 1 and not res.right

    N = 100
    inorder, preorder = [], []
    for i in range(N):
        inorder.append(i)
        preorder.append((N - 1) - i)

    res = binary_tree_from_preorder_inorder(preorder, inorder)
    assert res.data == N - 1 and res.left.data == N - 2 and not res.right


def main():
    simple_test()
    for times in range(1000):
        print(times)
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 10000)
        root = generate_rand_binary_tree(n, True)
        pre_order = generate_preorder(root)
        in_order = generate_inorder(root)
        res = binary_tree_from_preorder_inorder(pre_order, in_order)
        assert is_two_binary_trees_equal(root, res)


if __name__ == '__main__':
    main()