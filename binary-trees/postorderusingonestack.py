#postordertraversal using one stack

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

def peek(stack):
  if(len(stack) > 0):
    return stack[len(stack) - 1]
  return None
  
def postOrderTraversal(root):
  if(root is None):
    return;
  
  ans = []  
  s = []
  
  while(True):
    
    while(root is not None):
      if(root.right is not None):
        s.append(root.right)
      s.append(root)
      
      root = root.left
      
    root = s.pop()
    
    if(root.right is not None and peek(stack) == root.right):
      s.pop()
      s.append(root)
      root = root.right
    else:
      ans.append(root.val)
      root = None
      
    if(len(s) < 1):
      break;
      
  print(ans)
  
postOrderTraversal(root)
    