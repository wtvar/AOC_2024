file_name = "input.txt"
#file_name = "test.txt"

def check_higher(list):
    current = 0
    prior = 0
    higher = None
    for val in list:
        current = int(val)
        if prior == 0:
            prior = current
            pass
        elif current > prior and ((current - prior) <= 3):
            prior = current
            higher = True
        else:
            higher = False
            break
    #print(f'higher is: {higher}')
    return higher

def check_lower(list):
    current = 0
    prior = float('inf')
    higher = None
    for val in list:
        current = int(val)
        if prior == float("inf"):
            prior = current
            pass
        elif current < prior and ((prior - current) <= 3):
            prior = current
            higher = True
        else:
            higher = False
            break
    #print(f'lower is: {higher}')
    return higher

with open(file_name) as text:
    safe = 0
    for line in text:
        data = line.strip().split('\n')
        current = 0
        prior = 0
        line_list = data[0].split(" ")
        #print(line_list)
        if check_higher(line_list):
            safe += 1
        elif check_lower(line_list):
            safe += 1

        else:
            
            print('CHECKING FOR SPECIAL CASE')
            print(f'current safe: {safe}')
            
            for key, val in enumerate(line_list):
                print(f' full list {line_list}')
                new_list = line_list.copy()
                new_list.pop(key)
                print(f'checking shorter: {new_list}')
                if check_higher(new_list):
                    safe += 1
                    break
                elif check_lower(new_list):
                    safe += 1
                    break
            print(f'safe now: {safe}')
            print("-----------------------------")
        #print(f'running safe total: {safe}')

    print(f'final safe: {safe}')

"""test = ['72 73 75 77 78 80 81']
line_list = test[0].split(" ")
print(check_lower(line_list))
"""
