
from rich import print
from rich import traceback
import re
# load the rich stuff
traceback.install()

file_name = "input.txt"

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

total = 0

with open(file_name) as text:
    for line in text:
        #print(line)
        #print(type(line))
        matches = re.findall(pattern,line)
        for match in matches:
            if match:
                
                added = (int(match[0]) * int(match[1]))
                #print(f'adding: {added}')
                total += added
                #print(f'new total: {total}')

    print(total)    
        
        
        
        
        

"""# Method 1: findall() - returns list of tuples
matches_findall = re.findall(pattern, test_string)
print("re.findall() results:")
for match in matches_findall:
    print(f"x = {match[0]}, y = {match[1]}")
"""


# Test strings
test_strings = [
    "mul(123,456)",   # Valid
    "mul(1,999)",     # Valid
    "mul(42,7)",      # Valid
    "mul(1234,5)",    # Invalid (first number > 3 digits)
    "mul(1,5000)"     # Invalid (second number > 3 digits)
]

"""
for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        x, y = match.groups()
        print(f"Match found: x = {x}, y = {y}")
    else:
        print(f"No match for: {test_string}")
        
        """
