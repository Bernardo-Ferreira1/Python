# Define a class to represent a node in the binary search tree
class TreeNode:

    def __init__(self, key):
        # Initialize a node with a key (value)
        self.key = key  # The value stored in this node
        self.left = None  # Pointer to the left child (initially None)
        self.right = None  # Pointer to the right child (initially None)

    def __str__(self):
        # Define a string representation of the node, which will return the key as a string
        return str(self.key)

# Define a class to represent the binary search tree (BST)
class BinarySearchTree:

    def __init__(self):
        # Initialize the BST with an empty root (no nodes in the tree yet)
        self.root = None

    # Private helper method to insert a key into the tree recursively
    def _insert(self, node, key):
        # If the current node is None, we have found the position to insert the new key
        if node is None:
            # Create a new TreeNode and return it
            return TreeNode(key)

        # If the key to insert is smaller than the current node's key,
        # recursively insert it into the left subtree
        if key < node.key:
            node.left = self._insert(node.left, key)
        # If the key to insert is larger than the current node's key,
        # recursively insert it into the right subtree
        elif key > node.key:
            node.right = self._insert(node.right, key)

        # Return the node after potential updates
        return node

    # Public method to insert a new key into the tree
    def insert(self, key):
        # Start the insertion process at the root of the tree
        self.root = self._insert(self.root, key)

    # Private helper method to search for a key in the tree recursively
    def _search(self, node, key):
        # If the current node is None (not found) or matches the key, return the node
        if node is None or node.key == key:
            return node

        # If the key is smaller than the current node's key, search in the left subtree
        if key < node.key:
            return self._search(node.left, key)
        # Otherwise, search in the right subtree
        return self._search(node.right, key)

    # Public method to search for a key in the tree
    def search(self, key):
        # Start the search process at the root of the tree
        return self._search(self.root, key)

    # Private helper method to delete a key from the tree recursively
    def _delete(self, node, key):
        # If the current node is None, the key is not found, so return None
        if node is None:
            return node

        # If the key to delete is smaller than the current node's key,
        # recursively search and delete it from the left subtree
        if key < node.key:
            node.left = self._delete(node.left, key)
        # If the key to delete is larger than the current node's key,
        # recursively search and delete it from the right subtree
        elif key > node.key:
            node.right = self._delete(node.right, key)
        # If the key matches the current node's key, this is the node to delete
        else:
            # Case 1: Node has no left child, replace it with its right child
            if node.left is None:
                return node.right
            # Case 2: Node has no right child, replace it with its left child
            elif node.right is None:
                return node.left

            # Case 3: Node has two children
            # Find the smallest key in the right subtree (inorder successor)
            node.key = self._min_value(node.right)
            # Delete the inorder successor from the right subtree
            node.right = self._delete(node.right, node.key)

        # Return the updated node
        return node

    # Public method to delete a key from the tree
    def delete(self, key):
        # Start the deletion process at the root of the tree
        self.root = self._delete(self.root, key)

    # Private helper method to find the smallest key in a subtree
    def _min_value(self, node):
        # Traverse the left subtree to find the leftmost (smallest) node
        while node.left is not None:
            node = node.left
        # Return the key of the leftmost node
        return node.key

    # Private helper method for inorder traversal of the tree (left-root-right)
    def _inorder_traversal(self, node, result):
        if node:  # If the current node is not None
            # Traverse the left subtree recursively
            self._inorder_traversal(node.left, result)
            # Append the current node's key to the result list
            result.append(node.key)
            # Traverse the right subtree recursively
            self._inorder_traversal(node.right, result)

    # Public method to perform an inorder traversal of the tree
    def inorder_traversal(self):
        # Create an empty list to store the traversal result
        result = []
        # Start the inorder traversal process from the root
        self._inorder_traversal(self.root, result)
        # Return the list of keys in sorted order
        return result

# Example usage of the BinarySearchTree
bst = BinarySearchTree()

# Define a list of keys to insert into the tree
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert each key into the tree
for node in nodes:
    bst.insert(node)

# Search for a key (80) in the tree and print the result
print('Search for 80:', bst.search(80))

# Perform an inorder traversal of the tree and print the result
print("Inorder traversal:", bst.inorder_traversal())

# Delete a key (40) from the tree
bst.delete(40)

# Search for the deleted key (40) to verify its removal
print("Search for 40:", bst.search(40))

# Perform an inorder traversal after deletion and print the result
print('Inorder traversal after deleting 40:', bst.inorder_traversal())