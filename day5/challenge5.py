
import sys
import fileinput
import re


def bitoperator(string, char, value):
    for i, letter in enumerate(string):
        if letter == char:
            value = value ^ 1 << i
    return value

def getseats(rowmap):
    row = bitoperator(rowmap[6::-1], 'F', 127)
    col = bitoperator(rowmap[:6:-1], 'L', 7)
    return row*8+col

def getmissingNum(list):
    start = list[0]
    end = list[-1]
    #only work because there is only one missing num
    expectedsum = sum(x for x in range(start, end+1) )
    realitysum = sum(list)
    return (expectedsum-realitysum)



if __name__ == "__main__":
    results = [getseats(line.rstrip()) for line in fileinput.input()]
    results.sort()
    print ("Max", results[-1])
    print ("Missing", getmissingNum(results))
