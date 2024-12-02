file_name = "input.txt"


        
def check_higher(list):
	current = 0
	prior = 0
	higher = None
	for val in list:
		current = int(val)
		if prior == 0:
			prior = current
			pass
			
		elif current > prior and ((current -  prior) <= 3):
			prior = current
			higher = True
		else: 
		    higher = False
		    break
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
	return higher
			
		
with open(file_name) as text:
    safe = 0
    for line in text:
        data = line.strip().split('\n')
        print(data)
        current = 0
        prior = 0
        line_list = data[0].split(" ")
        if check_higher(line_list):
        	safe += 1
        elif check_lower(line_list):
        	safe += 1
        print(f'safe: {safe}')
        	
    print(f'final safe: {safe}')
		
        



"""test = ['72 73 75 77 78 80 81']
line_list = test[0].split(" ")
print(check_lower(line_list))
"""
