
import sys
import fileinput
import re
import copy

pattern = r"(\w{3})\s(\+|-)(\d+)"
prog = re.compile(pattern)

def parse(row):
    instru, sign, steps = prog.match(row).groups()
    return [instru, sign, steps, 0]
    
def steptiny(index, count, lists):
    if (index == len(lists)-1):
        return (count, index)
    if "*" in lists[index]:
        return (count, index)
    instru = lists[index][0]
    sign = lists[index][1]
    amount = lists[index][2]
    marker = "*"
    lists[index].append(marker)
    if instru == 'acc':
        count = count + add(sign, int(amount))
        index = index + 1
    if instru == "jmp":
        index = index + add(sign, int(amount))
    if instru == "nop":
        index = index + 1
    return (steptiny(index, count, lists))

def add(sign, value):
    if sign == '+':
        return value
    else:
        return value*(-1) 

if __name__ == "__main__":
    results = [parse(line.rstrip()) for line in fileinput.input()]
    allowed = 1
    print (steptiny(0,0,results))

