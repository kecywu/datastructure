# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def hash_function(s):
    x = 31
    prime = 10**9+7
    
    # choose a prime larger than |P||T| to avoid exceeding time limit
    
    ans = 0
    for c in reversed(s):
        ans = (ans*x + ord(c)) % prime
    
    return ans

def precompute_hash(pattern,text):
    x = 31 # this doesn't matter
    prime = 10**9 + 7 # this matters
    
    H = [0]*(len(text)-len(pattern)+1)
    s = text[len(text)-len(pattern):len(text)]
    
    H[len(text)-len(pattern)] = hash_function(s)
    
    
    y = 1
    for i in range(1,len(pattern)+1):
        y = (y*x) % prime
    
    for i in range(len(text)-len(pattern)-1,-1,-1):
        H[i] = (x*H[i+1] + ord(text[i]) - y*ord(text[i+len(pattern)]) + prime) % prime
    
    return H
    
    

def get_occurrences_fast(pattern,text):
    result = []
    
    phash = hash_function(pattern)
    for i in range(0,len(text)-len(pattern)+1):
        thash = hash_function(text[i:i+len(pattern)])
        
        if phash != thash:
            continue
        else:
            if pattern == text[i:i+len(pattern)]:
                result.append(i)
    
    return result

# pre-compute hash - you need this to pass the grader
def get_occurrences_faster(pattern,text):
    result = []
    
    phash = hash_function(pattern)
    H = precompute_hash(pattern,text)
    
    for i in range(0,len(text)-len(pattern)+1):
      
        if phash != H[i]:
            continue
        else:
            if pattern == text[i:i+len(pattern)]:
                result.append(i)
    
    return result
    

if __name__ == '__main__':
    print_occurrences(get_occurrences_faster(*read_input()))

