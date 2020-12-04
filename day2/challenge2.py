
import sys
import fileinput
from typing import List
import re


class Parser():

    def __init__(self, regex_pattern, policy):
         self.pattern = regex_pattern
         self.policy = self.get_policy(policy)

      
    def set_policy(self, policy):
         self.policy = self.get_policy(policy)
         return self

    def process(self):
        sum = 0
        for line in fileinput.input():
            min, max, letter, string = self.regeex_parser(line.rstrip())
            if self.policy(int(min), int(max), letter, string):
                sum+=1
        return sum

    def regeex_parser(self, line):
        return re.split(self.pattern, line)

    def get_sum(self):
        return (self.process())

    def get_policy(self, policy):
        if policy == 1:
            return self._policy_one  
        elif policy == 2:
            return self._policy_two
        else:
            raise ValueError(policy)

    def _policy_one(self, min, max, letter, string):
        count = string.count(letter)
        return True if count >= min and count <= max else False

    def _policy_two(self, min, max, letter, string):
        if (string[min-1] == letter) != (string[max-1] == letter):
            return True
        return False

    




if __name__ == "__main__":
    parser = Parser('-|:?\s',1)
    print("first", parser.get_sum())
    print("second", parser.set_policy(2).get_sum())
