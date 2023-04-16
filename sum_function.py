array = [1,2, 3,4,5,9,10]

def sum_array(arr):
	return arr[0] + sum(arr[1:])
def count_items(arr):
	if arr == []:
		return 0
	else:
		return 1 + count_items(arr[1:])
		
		
	
print(count_items(array))
