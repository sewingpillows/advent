
import sys
import fileinput
import re



def clean_baggage(line_item):
    clean_item = []
    for item in line_item:
        count, *d  = re.findall('(\d*)\s?(\w*)\s(\w*)\sbags?.?', item)[0]
        clean_item.append((count or 0, ''.join(d)))
    return clean_item

def map_baggage(baggage_list):
    mapping = {}
    for x in baggage_list:
        parent_bag = x[0][1]
        results = set.union(*[{y} for y in x[1:]])
        if parent_bag in mapping:
            mapping[parent_bag] = set.union(results,mapping[x[0]]) 
        else:
            mapping[parent_bag] = results
    return mapping


def part1(mapping, key):
    return sum([key_count(item, mapping) for item in mapping if item!=key])

def key_count(item_name, mapping):
    if item_name == "noother" or item_name not in mapping:
        return False
    if item_name == 'shinygold':
        return True
    for value in mapping[item_name]:
        result = key_count(value[1], mapping)
        #stop search if found and return
        if result:
            return result
    return False
        
def part2(mapping, key):
    if key not in mapping:
        return 1
    final_count = 0
    item = mapping[key]
    for count, color in mapping[key]:
        final_count = int(count) + int(count)*part2(mapping, color) + final_count
    return final_count


if __name__ == "__main__":
    cleaned_baggage = [clean_baggage(re.split('contain|,', line.rstrip())) for line in fileinput.input()]
    mapped_baggage = map_baggage(cleaned_baggage)
    print(part1(mapped_baggage, 'shinygold'))
    print(part2(mapped_baggage, 'shinygold'))

