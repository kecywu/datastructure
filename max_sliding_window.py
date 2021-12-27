# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_window(sequence,m):
    maximums = []
    
    if len(sequence) == 0 or m == 0:
        return
    
    if m > len(sequence):
        return
    
    if m == 1:
        return sequence
    
    q = deque()
    l = 0
    r = 0
    
    while r < len(sequence):
        
        # pop left
        if q and l > q[0]:
            q.popleft()
            
            
        # append, pop all smaller values
        while q and sequence[q[-1]] < sequence[r]:
            q.pop()
        q.append(r)
    
            
        # check length
        if r + 1 >= m:
            maximums.append(sequence[q[0]])
            l += 1
        
        r += 1
    
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

#    print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))
# * represent arbitrary number of inputs (no list format)
