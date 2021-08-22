def binary_search_iterative(arr: list, el: int) -> int:
    """
    Search for an element `el` in the sorted list `arr`.
    Return the index of element if found, else -1
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == el:
            return mid
        elif arr[mid] < el:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr: list, el: int, low: int, high: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == el:
        return mid
    elif arr[mid] < el:
        return binary_search_recursive(arr, el, mid + 1, high)
    else:
        return binary_search_recursive(arr, el, low, mid - 1)


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    li = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90]

    assert binary_search_iterative(l, 11) == binary_search_recursive(
        l, 11, 0, len(l) - 1
    )
    assert binary_search_iterative(li, 7) == binary_search_recursive(
        li, 7, 0, len(li) - 1
    )
