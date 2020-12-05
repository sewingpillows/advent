
import sys
import fileinput
import re


def validPassport(p):
    rules = {
        'ecl': (lambda a: len(re.findall('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', a)) == 1),
        'iyr': (lambda a: int(a) >= 2010 and int(a) <= 2020),
        'pid': (lambda a: len(re.findall('^[\d]{9}$', a)) == 1),
        'eyr': (lambda a: int(a) >= 2020 and int(a) <= 2030),
        'hgt': (lambda a: len(re.findall('^1([5-8][0-9]|[9][0-3])cm$|^(59|6[0-9]|7[0-6])in$', a)) == 1),
        'byr': (lambda a: int(a) >= 1920 and int(a) <= 2002),
        'hcl': (lambda a: len(re.findall('^#([\d|\w]{6})$', a)) == 1),
        'cid': (lambda a: True),
    }
    return (all([rules[row[0]](row[1]) for row in re.findall('([a-zA-Z]{3}):(\S+)', p)]))


def cleanPassport(p):
    pp = {'ecl': False, 'iyr': False, 'pid': False,
          'eyr': False, 'hcl': False, 'byr': False, 'hgt': False}
    for row in re.findall('([a-zA-Z]{3}):(\S+)', p):
        pp.update({row[0]:True}) 
    return (all(x == True for x in pp.values()))


if __name__ == "__main__":
    file = open('input', 'r')
    #trying list comprehension, which I think is incomprehensible
    clean = [p for p in (x.replace('\n', ' ') for x in file.read().split('\n\n')) if cleanPassport(p)]
    print ('part 1', len(clean))
    valid = sum([validPassport(p) for p in clean])
    print('part 2', valid)
