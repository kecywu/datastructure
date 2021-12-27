# python3

import sys
import threading


#def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height
    
    # depth = {-1:0}
    # while len(depth) <= n:
    #     for child, parent in enumerate(parents):
    #         if parent in depth:
    #             depth[child] = depth[parent] + 1
    # return max(depth.values())
    
    # make it a class and memorize height as a class field
    # don't use recursion, loop through all the nodes



def build_tree(n,parents):
    tree = [0]*n
    root = int
    
    for i in range(n):
        tree[i] = []
    
    for i in range(n):
        parent = parents[i]
        
        if parent == -1:
            root = i
            
        else:
            tree[parent].append(i)
            
    return tree, root

#walk tree while updating both stacks (adding children to the walk stack and 
#adding children's level to height/depth stack), and comparing most recently added height stack value 
#to current maxheight.

def compute_height(tree,root):

    if not tree:
        return 0
    
    stack = [root]
    height = [1]
    maxheight = 0
    
    while stack:
        node = stack.pop()  # stores current node that you are on
        depth = height.pop() # stores current level
        
        if len(tree[node]) > 0:
            depth += 1
            for i in range(len(tree[node])):
                stack.append(tree[node][i])
                height.append(depth)
                print(stack)
                print(height)
        
    maxheight = height.pop()

    return maxheight

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree, root = build_tree(n, parents)
#    print(tree,root)
    print(compute_height(tree,root))


if __name__ == "__main__":
    main()


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
  
 