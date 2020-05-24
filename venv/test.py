
'''
for x in reversed(range(4)):
	for y in range(x+1):
		print('# ', end = "")
	print("")
'''
import array as arr
import numpy as np

def findPrimeNumber(num):
	for x in range(2,num):
		if num != x and num%x == 0:
			return 'NOT a Prime'
	else:
		return 'Prime'
'''
for y in range(100):
    value = findPrimeNumber(y)
    print(f"the number {y} is {value}")
'''
x_array = np.array(['1123','dadfasdf','coffe'])

for e in x_array:
    print(e)

y_array = arr.array('i',[])

n = int(input("Enter how many values do you want to insert : "))

for i in range(n):
    in_value = int(input("Enter the next value : "))
    y_array.append(in_value)


print(len(y_array))
'''
value = int(input("Enter the value of the search : "))
if np.y_array.index(value) > 0:
    print('value found in the array by index search')
else:
    print('value not found in the array by index search')

for i in range(n):
    if value == (y_array[i]):
        print("value found in the array")
        break
else:
    print("value not found in the array")
    '''
