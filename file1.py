import random
import time

# Node for Binary Search Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary Search Tree Class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

# AVL Tree Node
class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

# AVL Tree Class (Balanced BST)
class AVLTree(BinarySearchTree):
    def _insert(self, root, key):
        if root is None:
            return AVLNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        # Update height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        # Perform rotations if unbalanced
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        if z.right is None:
            return z  # No rotation if the right child does not exist

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def right_rotate(self, z):
        if z.left is None:
            return z  # No rotation if the left child does not exist

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

if __name__ == "__main__":
    # Task 1: Compare Data Structures
    numbers = []
    bst = BinarySearchTree()
    avl = AVLTree()
    for _ in range(150000):
        num = random.randint(1, 1000000)
        numbers.append(num)
        bst.insert(num)
        avl.root = avl._insert(avl.root, num)

    # Search functionality (optional)
    # Example: Searching a random number in all three structures
    search_number = random.choice(numbers)
    print(f"Searching for number: {search_number}")

    # Search in list
    list_start_time = time.perf_counter()
    found_in_list = search_number in numbers
    list_end_time = time.perf_counter()
    list_search_time = list_end_time - list_start_time

    # Search in BST
    bst_start_time = time.perf_counter()
    found_in_bst = bst.search(search_number)
    bst_end_time = time.perf_counter()
    bst_search_time = bst_end_time - bst_start_time

    # Search in AVL
    avl_start_time = time.perf_counter()
    found_in_avl = avl.search(search_number)
    avl_end_time = time.perf_counter()
    avl_search_time = avl_end_time - avl_start_time

    # Output results
    print(f"List Search Time: {list_search_time:.6f} seconds - Found: {found_in_list}")
    print(f"BST Search Time: {bst_search_time:.6f} seconds - Found: {found_in_bst}")
    print(f"AVL Search Time: {avl_search_time:.6f} seconds - Found: {found_in_avl}")
