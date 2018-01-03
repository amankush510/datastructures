 #Diagonal Traversal

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

res = dict()



def diagonalTraversal(root, slope, res):
  if(root is None):
    return;
  if(slope not in res):
    res[slope] = []
  res[slope].append(root.val)
    
  diagonalTraversal(root.left, slope - 1, res)
  diagonalTraversal(root.right, slope, res)
  
  return res
  
print(diagonalTraversal(root, 1, res))

print(res)



  

  
  
  
    


  

  
  
  
    