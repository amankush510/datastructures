 #Construct tree from inorder and preorder

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
inOrder = [4, 2, 5, 1, 6, 3, 7]
preOrder = [1, 2, 4, 5, 3, 6, 7]

def peek(stack):
  if(len(stack) > 0):
    return stack[-1]
  return None

def searchInInorder(inOrder, x, inStart, end):
  for i in range(inStart, end + 1):
    if(inOrder[i] == x):
      return i
  return -1

preStart = 0
  
def constructTree(inOrder, preOrder, inStart, inEnd):
  if(inStart > inEnd):
    return None
  
  global preStart;
  cur = Node(preOrder[preStart])
  preStart = preStart +1
    
  if(inStart == inEnd):
    return cur
    
  index = searchInInorder(inOrder, cur.val, inStart, inEnd)
  
  cur.left = constructTree(inOrder, preOrder, inStart, index - 1)
  cur.right = constructTree(inOrder, preOrder, index + 1, inEnd)
  
  return cur
  
def printInOrder(root):
  if root is None:
    return
  
  printInOrder(root.left)
  print(root.val)
  printInOrder(root.right)
  
root = constructTree(inOrder, preOrder, 0, len(inOrder) - 1)
printInOrder(root)


  

  
  
  
    