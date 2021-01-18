
import sys
import fileinput
import re


def inter(list):
    clean  = set.intersection(*[set(x) for x in list])
    return len(clean)


if __name__ == "__main__":
    file = open('input', 'r')
    clean_input = [x for x in file.read().split('\n\n')]
    clean = sum([len(set(x.replace('\n', ''))) for x in clean_input])
    print ("part 1", clean)
    file = open('input', 'r')
    clean = [inter(x.split('\n')) for x in clean_input]
    print ("part 2", sum(clean))
