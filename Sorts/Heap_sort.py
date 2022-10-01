# Heap sort
# Time Complexity: O(nlog(n))

def heapify(arr, n, p):
    # p is parent node
    maximum = p
    l = 2*p + 1     # left node = 2*p + 1
    r = 2*p + 2     # right node = 2*p + 2

    if l < n and arr[p] < arr[l]:
        maximum = l

    if r < n and arr[maximum] < arr[r]:
        maximum = r

    if maximum != p:
        # perform swapping to push the largest element to the back
        arr[p], arr[maximum] = arr[maximum], arr[p]
        heapify(arr, n, maximum)


def heap_sort(arr, n):
    # building a max heap
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # perform swapping to push the largest element to the back
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def main():
    arr = [5, 2, 4, 6, 1, 3]
    print(heap_sort(arr, len(arr)))


if __name__ == '__main__':
    main()
