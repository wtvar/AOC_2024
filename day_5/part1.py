
from rich import print
from rich import traceback
import re
from tqdm import tqdm

# load the rich stuff
traceback.install()

file_name = "input.txt"

total = 0


def rule_check(rules):
    rule_list = {}
    for line in rules.strip().split('\n'):
        first, second = line.strip().split('|')
        
        # If the second number is already a key, append the first number to its list
        if second in rule_list:
            rule_list[second].append(first)
        # If the second number is not yet a key, create a new list with the first number
        else:
            rule_list[second] = [first]
    
    return rule_list

def find_keys_by_value(dictionary, search_value):
    matching_keys = []
    for key, values in dictionary.items():
        if search_value in values:
            matching_keys.append(key)
    return matching_keys
    

    
with open(file_name) as text:
    
    grid = [row for row in text.read().strip().split('\n\n')]
    rules = grid[0]
    updates = grid[1]
    rule_dict = rule_check(rules)
    #print(f'rules: {rule_dict}')
    #print(updates)
    #print('......................')
    for line in tqdm(updates.strip().split('\n')):
        l = [var for var in line.split(',')]
        
        #print(f'l is: {l}')
        valid = True
        for key,char in enumerate(l):
            #print(f'char: {char}')
            
            #this looks for characters that come before the value in "char"
            search_range = l[:key]
            new_search_range = l[key:]
            #print(f'search: {search_range}')
            
            for char in search_range:
                if char in rule_dict:
                    target_rule = rule_dict[char]
                    #print(f'rule found: {target_rule}')
                    for rule in target_rule:
                        if rule in search_range:
                            #print(f'rule {rule} is adhered to: {target_rule}')
                            pass
                        elif rule in new_search_range:
                            #print(f'rule {rule} is NOT adhered to: {target_rule} in {new_search_range}')
                            valid = False
                            break
                        else:
                            pass
            #print(f'valid: {valid}')
            
        if valid:
            mid = mid_value = l[len(l)//2]
            #print(f'mid: {mid} of l: {l}')
            total += int(mid)
           
    
    
    print(f'total: {total}')

