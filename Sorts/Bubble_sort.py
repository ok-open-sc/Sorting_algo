# Bubble sort algorithm

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    arr = [4, 5, 1, 2, 3]
    print(bubble_sort(arr))

if __name__ == "__main__":
    main()
