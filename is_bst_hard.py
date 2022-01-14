#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
      return True
  
  tree_list,tree_node = inOrderTraversal(tree,0,result=[],nodes=[])
  
  if len(tree_list) == 1:
      return True
  else:
      for i in range(len(tree_list)-1):
          if tree_list[i] < tree_list[i+1]:
              continue
          elif tree_list[i] == tree_list[i+1]:
              if tree[tree_node[i]][2] == -1:  # only need to check if previous node has a right child
                  return False
          else:
              return False
  
  return True
  

def inOrderTraversal(tree,index,result,nodes):
    
    if index == -1:
        return
    
    inOrderTraversal(tree,tree[index][1],result,nodes)
    
    result.append(tree[index][0])
    nodes.append(index)
    
    inOrderTraversal(tree,tree[index][2],result,nodes)
    
    return result, nodes



def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
