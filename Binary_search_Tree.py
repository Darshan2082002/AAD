# Binary Search Tree
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def insert(root, data):
    if root is None:
        return Node(data)
    if data == root.data:
        return root
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
def search(root,data):
    if root is None or root.data==data:
        return root

    if data < root.data:
        return search(root.left, data)
    else:
        return search(root.right,data)
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr
def delete(root,data):
    if root is None:
        return root
    if data <root.data:
        root.left=delete(root.left,data)
    elif data > root.data:
        root.right=delete(root.right,data)
    else:
        if root.left is None:
            return root.right 
        if root.right is None:
            return root.left
        succ=get_successor(root)
        root.data=succ.data
        root.right=delete(root.right,succ.data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
            

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    x = 15

    root = delete(root, x)
    inorder(root)
    print()
# Searching for keys in the BST
print("Found" if search(root, 19) else "Not Found")
print("Found" if search(root, 80) else "Not Found")