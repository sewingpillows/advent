
import sys
import fileinput
import re

def ski(down, over, hill):
    width = len(hill[0])
    tree = 0
    for i in range(down, len(hill), down):
        index = int(i*(over/down)) % width
        #print(hill[i], index, hill[i][index],i)
        if hill[i][index] == '#':
            #print ("FOUND")
            tree +=1
    return tree


if __name__ == "__main__":
    skihill =   [line.rstrip() for line in fileinput.input()]
    part1 = ski(1, 3, skihill)
    print ('part1', part1)
    print ('part2', part1 * ski(1, 1, skihill) * ski(1, 5, skihill) * ski(1, 7, skihill) * ski(2, 1, skihill))