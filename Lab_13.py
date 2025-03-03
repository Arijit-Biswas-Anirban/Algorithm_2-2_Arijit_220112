# Lab 13: Tree Traversing 

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

def create_tree():
    val = input("Enter node value (or 'None' for no node): ")
    if val.lower() == "none":
        return None
    
    node = Node(int(val))
    print(f"Enter node value or 'none' for left child of {node.value}: ")
    node.left = create_tree()
    print(f"Enter node value or 'none' for right child of {node.value}: ")
    node.right = create_tree()
    
    return node

def pre_order(root):
    if root:
        print(root.value, end=" ")
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    if root:
        pre_order(root.left)
        print(root.value, end=" ")
        pre_order(root.right)

def post_order(root):
    if root:
        pre_order(root.left)
        pre_order(root.right)
        print(root.value, end=" ")
        
def main():
    root = create_tree()
    
    print(f"\nPre Order Traversal:\n")
    pre_order(root)
    print(f"\nIn Order Traversal:\n")
    in_order(root)
    print(f"\nPost Order Traversal:\n")
    post_order(root)

main()