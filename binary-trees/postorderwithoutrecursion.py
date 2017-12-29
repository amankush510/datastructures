#postorder without recursion

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

def postorderTraversal(root):
  if(root is None):
    return;
  s1 = []
  s2 = []
  
  s1.append(root)
  
  while(len(s1) > 0):
    current = s1.pop()
    s2.append(current)
    if(current != None):
      if(current.left is not None):
        s1.append(current.left)
      if(current.right is not None):
        s1.append(current.right)
        
  
  while(len(s2) > 0):
    current = s2.pop()
    print(current.val)
  
  

  
root = createTree()
root = None
postorderTraversal(root)
    