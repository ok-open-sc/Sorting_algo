# Selection sort
# Time Complexity = O(n^2)

def selection_sort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(selection_sort(alist))


if __name__ == '__main__':
    main()
