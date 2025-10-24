#binary tree implementation and functions
class Node:
    def __init__(self, node, left =None, right =None):
        self.node = node
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.node)
    
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.node] + inorder_traversal(root.right)
def preorder_traversal(root):
    if root is None:
        return []
    return [root.node] + preorder_traversal(root.left) + preorder_traversal(root.right)
def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.node]
def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
def is_balanced(root):
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


# Example usage:
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder Traversal:", inorder_traversal(root))
    print("Preorder Traversal:", preorder_traversal(root))
    print("Postorder Traversal:", postorder_traversal(root))
    print("Height of tree:", height(root))
    print("Total nodes in tree:", count_nodes(root))
    print("Is the tree balanced?", is_balanced(root))