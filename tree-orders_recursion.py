# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
#import resourceresource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


class TreeOrders:
  # attributes
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
      
  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return inOrderTraversal(self,index=0) 


  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return preOrderTraversal(self,index=0)

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return postOrderTraversal(self,index=0)

# functions
def inOrderTraversal(self,index):
    
    if index == -1:
        return
    inOrderTraversal(self,self.left[index])
    self.result.append(self.key[index])
    inOrderTraversal(self,self.right[index])
    
    return self.result 

def preOrderTraversal(self,index):
    
    if index == -1:
        return
    self.result.append(self.key[index])
    preOrderTraversal(self,self.left[index])
    preOrderTraversal(self,self.right[index])
    
    return self.result

def postOrderTraversal(self,index):
    
    if index == -1:
        return
    
    postOrderTraversal(self,self.left[index])
    postOrderTraversal(self,self.right[index])
    self.result.append(self.key[index])
    
    return self.result


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

if __name__ == "__main__":
    main()
    
threading.Thread(target=main).start()



    
    