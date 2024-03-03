def binary_search(arr, val, start, end):
    """Бінарний пошук для знаходження правильного місця вставки елемента у відсортований масив."""
    if start == end:
        return start if arr[start] > val else start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr):
    """Сортування вставками з бінарним пошуком."""
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


print("Sorted array:")
print(insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]))
