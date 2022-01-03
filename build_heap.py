# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps
# from i = n-1/2 to 1, sift down i (strictly less, children are 2i+1 and 2i+2)

def build_heapsort(data):
    
    swaps = []
    n = len(data)
    
    endindex  = n // 2 - 1
    
    # sift down
    for i in range(endindex,-1,-1):
        SiftDown(i,swaps,n,data)

    
    return swaps

# note 0-based index
def SiftDown(i,swaps,n,data):
    l = 2*i+1
    r = 2*i+2
    minindex = i
    
    if l <= n-1 and data[l] < data[minindex]:
        minindex = l
    
    if r <= n-1 and data[r] < data[minindex]:
        minindex = r
    
    if i != minindex:
        swaps.append((i,minindex))
        data[i], data[minindex] = data[minindex], data[i]
        SiftDown(minindex,swaps,n,data)
    

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heapsort(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    
 #   print(data)

if __name__ == "__main__":
    main()


