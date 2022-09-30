# Merge sort algorithm

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result

if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))
