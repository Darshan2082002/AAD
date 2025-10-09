class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
def get_height(root):
    if root is None:
        return 0   
    return root.height
def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left)-get_height(root.right)
def right_rotate(y):
    if y is None:
        return y
    x=y.left
    T=x.right
    x.right=y
    y.left=T
    y.height=1+max(get_height(y.left),get_height(y.right))
    x.height=1+max(get_height(x.left),get_height(x.right))
    return x
def left_rotate(x):
    if x is None:
        return x
    y=x.left
    T1=y.right
    y.right=x
    x.left=T1
    x.height=1+max(get_height(x.left),get_height(x.right))
    y.height=1+max(get_height(y.left),get_height(y.right))
    return y
def insert(root,data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    elif data>root.data:
        root.right=insert(root.right,data)
    root.height=1+max(get_height(root.left),get_height(root.right))
    balance=get_balance(root)
    if balance>1:
        if data<root.left.data:
            return right_rotate(root)
        else:
            root.left=left_rotate(root.left)
            return right_rotate(root)
        if balance<-1:
            if data>root.right.data:
                return left_rotate(root)
            else:
                root.right=right_rotate(root.right)
                return left_rotate(root)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

inorder(root)




