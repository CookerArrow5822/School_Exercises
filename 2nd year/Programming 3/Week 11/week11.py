#q1 merge sort

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    result = []
    i = 0
    j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1

    while i < len(left_sorted):
        result.append(left_sorted[i])
        i += 1

    while j < len(right_sorted):
        result.append(right_sorted[j])
        j += 1

    return result

#q2 quick sort

def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    smaller = []
    equal = []
    greater = []

    for value in lst:
        if value < pivot:
            smaller.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)

    sorted_smaller = quick_sort(smaller)
    sorted_greater = quick_sort(greater)

    return sorted_smaller + equal + sorted_greater


#question 3 selection sort

def selection_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp

    return lst

#Question 4 insertion sort

def insertion_sort(lst):
    n = len(lst)

    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return lst

#question 5 bubble sort

def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return lst

if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]

    print("Original:", data)

    # Merge sort (returns a new sorted list)
    print("Merge sort:    ", merge_sort(data))

    # Quick sort (returns a new sorted list)
    print("Quick sort:    ", quick_sort(data))

    # Selection sort (sorts in-place, so copy data first)
    data_sel = data.copy()
    selection_sort(data_sel)
    print("Selection sort:", data_sel)

    # Insertion sort
    data_ins = data.copy()
    insertion_sort(data_ins)
    print("Insertion sort:", data_ins)

    # Bubble sort
    data_bub = data.copy()
    bubble_sort(data_bub)
    print("Bubble sort:   ", data_bub)