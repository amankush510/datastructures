 #countLeafNodes

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
  
  return root
  
root = createTree()

def countLeafNodes(root):
  if(root is None):
    return 0 
  
  if(root.left is None and root.right is None):
    return 1
  
  
  return countLeafNodes(root.left) + countLeafNodes(root.right)

print(countLeafNodes(root))