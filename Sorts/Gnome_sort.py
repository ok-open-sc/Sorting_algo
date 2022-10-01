def gnomeSort(array, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if array[index] >= array[index - 1]:
            index = index + 1
        else:
            array[index], array[index - 1] = array[index - 1], array[index]
            index = index - 1
    return array
 
array = [2, 5, 3, 7, 1, 0, 4]
n = len(array)
 
array = gnomeSort(array, n)

print "Sorted array:",
for i in array:
    print i,