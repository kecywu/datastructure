#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
      return True
  
  tree_list = inOrderTraversal(tree,0,result=[])
  
  return tree_list == sorted(tree_list)
  

def inOrderTraversal(tree,index,result):
    
    if index == -1:
        return
    
    inOrderTraversal(tree,tree[index][1],result)
    
    result.append(tree[index][0])
    
    inOrderTraversal(tree,tree[index][2],result)
    
    return result


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
