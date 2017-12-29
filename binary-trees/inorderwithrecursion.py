
#Inorder traversal recursion

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
root = None

def createTree():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.left.left = Node(5)
  root.left.right = Node(6)
  root.right.left = Node(7)
  root.right.right = Node(8)
  root.right.left.right = Node(9)
  return root
  
def inOrderTraversal(root):
  if root:
    inOrderTraversal(root.left)
    print(root.val)
    inOrderTraversal(root.right)
    
root = createTree()
inOrderTraversal(root)
  