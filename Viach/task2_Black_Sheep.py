# Looking for number with minor parity. 
# One 'odd' number in all 'even' list, or 'even' in 'odd'
lst = [0, 8, 2, 50, 13, 6, 34]

# 'odd' or 'even' testing by three first numbers. Zero is an even number by the way. 
# 000 001 010 100 sum < 2 : all 'even', target is 'odd'
# 011 101 110 111 sum >= 2 : all 'odd', target is 'even'
test_sum = lst[0] % 2 + lst[1] % 2 + lst[2] % 2
target = 1 if test_sum < 2 else 0
result = [x for x in lst if x%2 == target]
print('Innitial list:\n', lst)
print('Black Sheep is', result)