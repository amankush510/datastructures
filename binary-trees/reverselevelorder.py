#reverselevelordertraversal

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

def reverseLevelOrderTraversal(root):
  queue = []
  stack = []
  queue.append(root)
  
  while(len(queue) > 0):
    node = queue.pop(0)
    stack.append(node)
     
    if(node.right is not None):
      queue.append(node.right)
    if(node.left is not None):
      queue.append(node.left)
     
  while(len(stack) > 0):
    print(stack.pop().val)
  
  
    
reverseLevelOrderTraversal(root)
    