# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        bracket = Bracket(next,i+1)
        
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(bracket)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                opening_brackets_stack.append(bracket)
                break
            
            else:
                prev = opening_brackets_stack.pop().char
                if are_matching(prev,next) == False:
                    opening_brackets_stack.append(bracket)
                    break
            
    return opening_brackets_stack


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if not mismatch:
        print("Success")
    else: 
        bracket = mismatch.pop()
        print(bracket.position)


if __name__ == "__main__":
    main()
