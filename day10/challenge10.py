
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



def partone(results):
    results.sort()
    voltage = 0
    onejolt = 0
    threejolt = 0
    while results:
        joltdiff = results[0]-voltage
        if joltdiff == 1:
            onejolt = onejolt + 1
        if joltdiff == 3:
            threejolt = threejolt +1
        voltage = voltage + joltdiff
        results = results[1:]
    print (onejolt* (threejolt+1))


if __name__ == "__main__":
    results = [int(line.rstrip()) for line in fileinput.input()]
    partone(results)
    results.append(0)
    results.sort(reverse=True)
    mapping = {}
    print(results)
    for x, i in enumerate(results):
        #possible
        sum = 0
        if i+1 in mapping:
            sum = sum + mapping[i+1]
        if i+2 in mapping:
            sum = sum + mapping[i+2]
        if i+3 in mapping:
            sum = sum + mapping[i+3]
        if sum == 0:
            sum = 1
        mapping[i] = sum
    print(mapping[0])








