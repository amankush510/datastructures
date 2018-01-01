#levelordertraversal with recursion

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
  
root = createTree()

def levelOrderTraversal(root):
  h = height(root) + 1
  for i in range(1, h):
    printGivenLevel(root, i)
    print(",")
  
def printGivenLevel(root, level):
  if(root == None):
    return;
  if(level == 1):
    print(root.val)
  elif level > 1:
    printGivenLevel(root.left, level - 1)
    printGivenLevel(root.right, level - 1)
    
def height(root):
  if(root is None):
    return 0;
  else:
    lheight = height(root.left) + 1
    rheight = height(root.right) + 1
    
    if(lheight > rheight):
      return lheight
    return rheight
  
  
    
levelOrderTraversal(root)
    