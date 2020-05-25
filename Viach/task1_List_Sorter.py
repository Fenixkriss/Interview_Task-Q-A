# Task: Sorting the list (of string and numbers) with saved location according to the type of items.
# Example:
# 	Initial list:     yellow  white 2 5  green  red    6 1 
# 	Final sorted list: green   red   1 2  white  yellow 5 6

def list_sorter_ligth(lst_inn):
	# Main function - light version, only strings and numbers in list
	lst_out, lst_of_str, lst_of_num  = [], [], []
	# Sepparator str/num
	for x in lst_inn:
		lst_of_str.append(x) if type(x)==str else lst_of_num.append(x) 
	# Sorter
	lst_of_str.sort()
	lst_of_num.sort()
	# Mixer
	for x in lst_inn:
		lst_out.append(lst_of_str.pop(0)) if type(x) == str else lst_out.append(lst_of_num.pop(0)) 
	# Result	
	return lst_out	


def list_sorter_heavy(lst_inn):
	# Main function - resistant to defferent type of element exceptions
	# If unsupported elements (nested lists or tuples of dict) found they leave untouched 
	lst_out, lst_of_str, lst_of_num  = [], [], []
	for x in lst_inn:
		if type(x)==str :
			lst_of_str.append(x)
		elif type(x)==int or type(x)==float:
			lst_of_num.append(x)
		else: pass # Unsupported element found

	# Sorter
	lst_of_str = sorted(lst_of_str)
	lst_of_num = sorted(lst_of_num)

	# Mixer
	for x in lst_inn:
		if type(x) == str :
			lst_out.append(lst_of_str.pop(0))
		elif type(x)==int or type(x)==float:
			lst_out.append(lst_of_num.pop(0))
		else: 
			lst_out.append(x)
	# Result	
	return lst_out	

# --- main ---

initial_list = ['yellow','white', 2, 5,'green','red', 6, 1, 9 , 'apple', 0] 
sorted_list = list_sorter_ligth(initial_list) #function call
print('Innitial list:\n', initial_list)			
print('Sorted list:\n', sorted_list)

initial_list_2 = ['yellow','white', 2, 5,('black',7),'red', [5,'x'], 1, 9 , 'apple', 0] 
sorted_list = list_sorter_heavy(initial_list_2) #function call
print('Innitial list:\n', initial_list_2)			
print('Sorted list:\n', sorted_list)
