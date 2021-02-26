
import sys
import fileinput
import re
from itertools import combinations
from itertools import product

def part1(numbers, number):
    for index in range(number, len(numbers)-1):
        comb = combinations(numbers[index-number:index], 2)
        target = numbers[index]
        if (all([sum(combindation)!=target  for combindation in comb])):
            return target
        

        
def findCont(key, nums):
    start = 0
    end = 0
    sum = nums[start]
    while (sum != key):
        if sum < key:
            end += 1
            sum = sum + nums[end]
        else:
            sum = sum  - nums[start]
            start += 1
    t = sorted(nums[start:end])
    return (t[0]+ t[len(t)-1])
    

if __name__ == "__main__":
    results = [int(line.rstrip()) for line in fileinput.input()]
    number = 25
    num  = part1(results, number)
    print(num)
    print(findCont(num, results))

