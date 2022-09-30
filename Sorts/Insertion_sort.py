# Insertion sort
# Time Complexity: O(n^2)

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A

def main():
    A = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(A))

if __name__ == "__main__":
    main()
