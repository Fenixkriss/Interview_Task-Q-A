# Script that makes up the maximum possible number from a list of positive integers.
# Example 
# [70 8 20 1 13] -> 87020131
# We consider '12' as twelve not as '1' and '2' 

lst = [70, 8, 20, 1, 13]
# lst = [155, 83, 81, 20, 1, 13, 2, 15689] #Test list. Uncomment for test

# Make list of numbers as string
lst_str = []
[ lst_str.append(str(x)) for x in lst ]

# Sort
lst_str.sort(reverse = True)

# Concatenate and convert to int
result = int(''.join(lst_str))

print('Innitial list:\n', lst)	
print('Maximus', result)