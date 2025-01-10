def merge_sort(array):
    if len(array) <= 1:
        return array
mid = len(array) // 2 
left = array[:mid]
right = array[mid:]

left_sorted = merge_sort(left)
right_sorted = merge_sort(right)

return merge(left_sorted, right_sorted)

def merge(left, right):
sorted_array  = []
i = 0 
j = 0
while i < len(left) and j < len(right):
    if  left[i] < right[j]:
        sorted_array.append(left[i])
        i += 1
    else:
        sorted_array.append(right[j])
        j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
return sorted_array


