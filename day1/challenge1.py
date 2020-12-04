
import sys
import fileinput



def process_input():
    return [int(line) for line in fileinput.input()]

def find_pair(args, key):
    less = 0
    end = len(args)-1
    while (less < end):
        sum = args[less]+args[end]
        if (sum == key):
            return args[less]*args[end]
        # If sum is greater than key, 
        # then try the next greatest num
        if (sum > key):
            end -= 1
        # If sum is less than key, 
        # then try the next number smallest num
        else:
            less += 1
    return None

def find_triple(args, key):
    for i, value in enumerate(args):
        target = args[i]
        pair =  find_pair(args[i:], key-target)
        if (pair != None):
            return pair*target
    return None


if __name__ == "__main__":
    key = 2020
    num = process_input()
    num.sort()
    print("PAIR", find_pair(num, key))
    print("TRIPLE", find_triple(num, key))
