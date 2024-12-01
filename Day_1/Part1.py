file_name = "input.txt"

left_list = []
right_list = []
with open(file_name) as text:
    for line in text:
        data = line.strip().split('\n')
        
        new_data = data[0].strip().split("   ")
        #print(new_data)
        left_list.append(new_data[0])
        right_list.append(new_data[1])
        #print(f'l l: {left_list}')
        #print(f'r l: {right_list}')
        
        
        
        
        #print(new_data)
        
    #print(left_list)
    left_list.sort()
    right_list.sort()
    
    print(left_list[:6])
    print("_---------")
    print(right_list[:6])
    
    
    final = 0
    
    for key,val in enumerate(left_list):
    	print(f'val: {val}')
    	print(f'right: {right_list[key]}')
    	res = abs(int(val) - int(right_list[key]))
    	final += res
    	
    print(final)
