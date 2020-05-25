# Function that takes a sequence of dictionaries containing names and 
# returns names separated by commas, except for the last one connected via an ampersand.
# [{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}] -> 'John, Jack & Joe'
# [{'name': 'John'}, {'name': 'Jack'}] -> 'John & Jack' 
# [{'name': 'John'}] -> 'John'' 

def greeting(list_of_names):
	greet = ''
	for k,v in enumerate(list_of_names):
		if k == 0 :
			greet = v['name']
		elif k < (len(list_of_names)-1): 
			greet += ', ' + v['name']
		else :
			greet += ' & ' + v['name']
	return greet

# --- main ---

initial_list = [{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}]
#initial_lst = [{'name': 'John'}, {'name': 'Jack'}] # uncomment for test 
#initial_lst = [{'name': 'John'}] # uncomment for test 

result = greeting(initial_list) # function call

# Resulting string
print('Greetings,')
print(result)