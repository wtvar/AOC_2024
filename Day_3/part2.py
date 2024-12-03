
from rich import print
from rich import traceback
import re
# load the rich stuff
traceback.install()

file_name = "input.txt"



total = 0
def check_do_pattern(text):
    # If do() is found, return True
    # If don't() is found, return False
    # If neither is found, return True
    match = re.search(r'do\(\)|don\'t\(\)', text)
    
    if match:
        return match.group(0) == "do()"
    
    return True

def find_last_do_pattern(text):
    # Find all matches of do() or don't()
    matches = re.findall(r'do\(\)|don\'t\(\)', text)
    
    # If no matches, return True
    if not matches:
        return True
    
    # Check the last match
    return matches[-1] == "do()"
    
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
with open(file_name) as text:
    line = text.read()
    #print(line)
    #print(type(line))
    matches = re.finditer(pattern,line)
    for match in matches:
        if match:
            #print(f'match found: {match.group(0)} at pos: {match.start()}')
            do_dont = find_last_do_pattern(line[:match.start()])
            #print(f'checking str: {line[:match.start()]}')
            #print(do_dont)
            if do_dont:
                added = (int(match.group(1)) * int(match.group(2)))
                #print(f'adding: {added}')
                total += added
                #print(f'new total: {total}')

    print(total)    
        
        
        
        
